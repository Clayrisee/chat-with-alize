# Chat with Alize
Chat with Alize is an application to ask the question with AI powered Agent. 

## Getting Started

### Run Locally
#### Prerequisites
- Python >= 3.8
- Pip version == 23.1.2

#### Install Alize Package
You need to install the core package using this command.
```bash
pip install .
```
#### Setup Env Variable
You need to setup several environment variables such as:
- Google API Key
- Google Custom Search Engine ID
- OpenAI Key

Usefule Docs about how to create the API:
- [Google Custom Search Engine](https://www.teachthought.com/technology/custom-search-engine/)
- [End to End Custom Search](https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search)
- [How to create OpenAI Key](https://platform.openai.com/account/api-keys)

here's the example how to setup it:
```bash
export GOOGLE_API_KEY=<GOOGLE_API_KEY>
export GOOGLE_CSE_ID=<GOOGLE_CSE_ID>
export OPENAI_API_KEY=<OPENAI_API_KEY>
```

#### Run the UI
After you finish the installation, you can run the web UI using this command line.
```
streamlit run main.py
```

### Run via Dockerfile
First, you need to pull the image registry from docker hub.
```bash
docker pull <UPDATE-IMAGE-REGISTRY>
```

after you pull the docker images, you can execute this command line.
```bash
<WILL BE UPDATED LATER..>
```

## Development
To reduce complexity installation for development, you can use VSCode and install Remote [Container extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Then it will be automatically detect the docker file and create the environment. You can choose the option `open folder in container`

## Contact
If you have any feedbacks you can contact me on my social link:
- Email: ardikatamah@gmail.com
- Linkedin: https://www.linkedin.com/in/haikalardikatama/
- Twitter: https://twitter.com/hklard