
### Entering/Exiting the VM from local terminal

If your virtual machine is called `cs231-vm` then turn on the virtual machine

	gcloud compute instances start cs231-vm

Now SSH into the virtual machine

	gcloud compute ssh --zone=us-west1-b cs231-vm

Log out of the virtual machine

	logout

After successfully logging out, shut down the instance (and stop billing)

	gcloud compute instances stop cs231-vm


### Fixing permissions to install packages

If installing or updating packages is persistently throwing a permissions error

	cd ~
	conda clean --all 
	sudo chown -R [username]:[username] /home/shared
 

### Detaching sessions using GNU `screen`

SSH into the server, and then run

	screen

Now start your process as you would normally. To detach it, hit [Ctrl]+A and then [Ctrl]+D. You can now log out of the server

To re-enter, SSH back into the server and then run

	screen -r

If there are multiple living processes, you will be prompted to enter the process ID before resuming

Check to see what sessions are detached

	screen -list 

Kill any sessions without entering them

	screen -X -S [process id] quit


More instructions [here](http://orcaman.blogspot.com/2013/08/google-compute-engine-keeping-your.html)


### Accessing multiple Google Cloud projects on the same local computer

Make a new project on the Google Cloud Console and then enable the appropriate API for the project

Check that the new project is alive by running locally

	gcloud projects list

Can switch projects locally

	gcloud config set project my-project

Can set a default using the variable `$CLOUDSDK_CORE_PROJECT`

Can check current setup using

	gcloud config list


### Running speech recognition

File needs to be in WAV or FLAC format already

	 ffmpeg -i input.mp3 -ac 1 output.flac

Or, for a video

	 ffmpeg -i input.mp4 -ac 1 output.flac


The `-ac 1` flag ensures that there is only one audio channel, which is currently a requirement

For short snippets < 1 min long,

	gcloud ml speech recognize 'audio_file.flac' --language-code='en-US'

For longer snippets, 

	gcloud ml speech recognize-long-running 'audio_file.flac' --language-code='en-US' --async

This will return a [process ID], retrieve the transcript using 

	gcloud ml speech operations wait [process ID]


Can also give it a flag containining common words

	--hints=[HINTS,...]
	        A list of strings containing word and phrase "hints" so that the speech
	        recognition is more likely to recognize them. This can be used to
	        improve the accuracy for specific words and phrases, for example, if
	        specific commands are typically spoken by the user. This can also be
	        used to add additional words to the vocabulary of the recognizer. See
	        https://cloud.google.com/speech/limits#content.


--configuration, --account are other useful flags


curl -s -H "Content-Type: application/json" \
    -H "Authorization: Bearer "$(gcloud auth print-access-token) \
    https://speech.googleapis.com/v1p1beta1/speech:recognize \


### Run speech recognition with slightly more customizability


Create a bucket to store your FLAC files here: https://console.cloud.google.com/storage/browser
Upload the files via the web GUI

	gs://my-bucket-name/my_file.flac

From the command line

	gsutil cp my_file.flac gs://my-bucket-name

View a list of all buckets [here](https://console.cloud.google.com/storage/browser)

Now put your settings into a local file called `my_config.json`

	{
	  "config": {
	      "encoding":"FLAC",
	      "languageCode": "en-US",
	      "enableAutomaticPunctuation": true
	  },
	 "audio": {
	      "uri":"gs://my-bucket-name/my_file.flac"
	  }
	}


Now run on Google Cloud using `curl`

	curl -s -H "Content-Type: application/json" -H "Authorization: Bearer "$(gcloud auth print-access-token) https://speech.googleapis.com/v1p1beta1/speech:recognize -d @my_config.json

Note the `v1p1beta1` because, as of when this is being written, certain settings (like punctuation) are still in beta testing

Occasionally you need to re-authenticate

	gcloud auth application-default login


More info from documentation [here](https://cloud.google.com/speech-to-text/docs/basics)


Dump output into a text file:

	curl -s -H "Content-Type: application/json" -H "Authorization: Bearer "$(gcloud auth print-access-token) https://speech.googleapis.com/v1p1beta1/speech:recognize -d @my_config.json > "mm.json"


	{
	  "config": {
	      "encoding":"FLAC",
	      "languageCode": "en-US",
	      "enableAutomaticPunctuation": true,
	      "model": "command_and_search"
	  },
	 "audio": {
	     "uri":"gs://transcriptions-wg/output.flac"
	  }
	}


For audio files longer than 1 minute, make a different config file

	{
	  "config": {
	      "encoding":"FLAC",
	      "languageCode": "en-US",
	      "enableAutomaticPunctuation": true,
	      "model": "command_and_search",
	      "speechContexts" : {
	        "phrases":["Nernst","chemistry","Cu"]
	        }
	  },
	 "audio": {
	      "uri":"gs://transcriptions-wg/my_audio.flac"
	  }
	}

And run using

	curl -s -H "Content-Type: application/json" -H "Authorization: Bearer "$(gcloud auth print-access-token) https://speech.googleapis.com/v1/speech:longrunningrecognize -d @my_config.json

	curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d @my_config.json "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize"


This time, to get the output, need to use a GET request

	curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application json; charset=utf-8" "https://speech.googleapis.com/v1operations/your-operation-name" > "output.json"

Can parse the output JSON with the tool `jq`, which may be installed as

	brew install jq

Now fetch and concatenate all of the output text using

	cat output.json | jq '.response.results[].alternatives[0].transcript' > transcript.txt

More info on long audio files is [here](https://cloud.google.com/speech-to-text/docs/async-recognize#speech-async-recognize-gcs-gcloud)



### Merge above into a bash script

Make a bucket called `my_transcriptions`, and then install ffmpeg, gcloud, and jq on your local machine

Script takes one argument: `video_file.mp4'

	#!/bin/bash                                                                                                                                                 

	ffmpeg -i $1 -ac 1 my_audio.flac
	gsutil cp my_audio.flac gs://transcriptions-wg
	jq '.audio.uri = "gs://transcriptions-wg/my_audio.flac"' template.json > "$tmp" && mv "$tmp" template.json
	curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" -d @templa\
	te.json "https://speech.googleapis.com/v1p1beta1/speech:longrunningrecognize"

The parsing script takes a process ID argument and gets the transcript. It then empties the bucket, to avoid incurring long-term storage fees

	#!/bin/bash                                                                                                                                                 
	curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application json; charset=utf-8" "https://speech.go\
	ogleapis.com/v1p1beta1/operations/"$1 > output_raw.json
	cat output_raw.json | jq '.response.results[].alternatives[0].transcript' > my_transcript.txt
	gsutil rm gs://bucket/my_audio.flac


Run this script on the video `nernst2.mp4` using
	
	bash run_transcription.sh nernst2.mp4

A process ID number should be given.
After giving it some time to run, print the output using to "my_transcription.txt" using

	bash parse_transcription.sh [process ID]

Will throw a null error if transcription is not done yet.

