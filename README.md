

![screenshot](https://github.com/noarche/AutoPrompt/blob/main/source/AutoPrompt.gif?raw=true)



# ꧁꧂ 🔮AutoPrompt
### Over 100 billion unique prompt possibilities. 

*Actual number is closer to 8.254∗10^35*

 Chances of two people generating the same prompt is low/slim!

Create random prompts to help with learning how to generate AI art.


To Generate a prompt place a check in the boxes. 
Think of these boxes as containers with a bunch of random prompts.
The final prompt will be combined with a comma inbetween
the random strings pulled from the boxes,
You do not need to change check boxes to get a new random
prompt. 

More checkboxs selected = longer prompt. This doesnt nessacarily mean a higher quality outcome. 

Use this app and try to find your sweet spot keywords to build your own prompts. 

Compatible will all image generation platforms!! Paste the prompt into your favorite Al-image gen. platform. *If you are not running a local model using comfyui or A1111 or forge stay away from the erotic and uncensored checkboxes!*

### 🍀Bonus Prompts:

Feeling lucky? Leave all the boxes empty and press Generate for a random yet complete prompt that someone else has used to make a pretty cool image!


------------------------------------------------

# ꧁꧂ 🌐Download

Look for AutoPrompt-v1.3.exe above and click it to start download. Version of file will be diff. depending on how many new 
 updates since this was written. 

The .exe file is the only file you need to run this application as a user. 

(The other files are the source files used to create the .exe)

------------------------------------------------

# Support

## 🟢Is this a virus❔

No it is not a virus, that is a false positive. Anything compiled with pyinstaller will be flagged as potentially malicious. Pyinstaller is what turns the .py file into a .exe file and allows people to run python scripts as portable applications without the need to install python or any dependancies.  

Please scan the actual source, the file that ends with '.py' -  It will with no doubt be 100% clean on virustotal.  That being said I have provided instructions on how to build your own exe from the file you know is clean. 

☑️Tip for all questionable applications: 

*Running the application via [Sandboxie](https://sandboxie-plus.com/downloads/) or similar app will virutalize and protect your OS as if it was running on a virtual machine - [Sandboxie](https://sandboxie-plus.com/downloads/) can be used with any application or installation package thus another great tool to have.* 

## ꧁꧂ How to run on linux❔ 

*You are also able to run the app this way on windows by installing python on windows.* 

Clone this repo with git

    git clone https://github.com/noarche/AutoPrompt

Install pre-requsites with pip

    pip install tkinter

Change to the directory containing the Python script

    cd \AutoPrompt\source\

Run the Python script (version may be diff)

    python AutoPrompt-v1.3.py



## ꧁꧂ How to Compile your own .exe file❔ 

*You are able to build your own exe file from the source on a windows and linux machine. Follow the steps below, assuming you have already installed pip*

Clone this repo with git

    git clone https://github.com/noarche/AutoPrompt

Install pre-requsites with pip

    pip install tkinter

Change to the directory containing the Python script
  	
    cd \AutoPrompt\source\

Run the following command to use pyinstaller to build an executable from the souce. Verify your version # in command matchs the version in source  dir. 
     
     pyinstaller --onefile --add-data "parts/*;parts" -w AutoPrompt-v1.3.py

Pyinstaller will created a couple of directories and files. 

    The .exe you want is located in \source\dist\AutoPrompt-v1.3.exe

------------------------------------------------


## ꧁꧂ 📢Update Notes:


➡️V1.4
📌7/10/2024

    3 new check box options; Furries, Mood, Uncensored 
    Fixed small bug that now prompts will be more randomly pulled from checkbox containers. 
    MANY Additional prompts have been added to most of the existing checkbox containers.  
    Leave all check boxes empty and press generate to see a prompt that someone else has used to generate an image.


![noarche's GitHub stats](https://github-readme-stats.vercel.app/api?username=noarche&show_icons=true&theme=transparent)


## ꧁꧂ 🪙Drop a tip

    (BTC) address bc1qnpjpacyl9sff6r4kfmn7c227ty9g50suhr0y9j
    
    (ETH) address 0x94FcBab18E4c0b2FAf5050c0c11E056893134266
    
    (LTC) address ltc1qu7ze2hlnkh440k37nrm4nhpv2dre7fl8xu0egx





