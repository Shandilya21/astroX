![astroX](https://github.com/shandilya21/astroX/raw/master/logo.png)

## :rocket: astro X - AI Bot 
An AI bot designed to explore and study about Astronomy and developed using Rasa. Astronomy was always an exciting topics to almost everyone. Inspired by the beauty of space, the objective is to make the far-away stars, galaxies, planets more accessible to people who want to learn general questions about planets, space science and become connected to the night sky overhead.

## How to Install Rasa

``` Requires Python 3.6 - 3.7 and pip >= 19.0 ```.

* Rasa currently support 3.6 - 3.7 version You can install Rasa Open Source using pip. Before proceeding for Rasa, kindly setup the enviornment as mention below

#### Create a virtual env using __virtualenv__ (Ubuntu)
* Create a virtual enviornment selecting python intrepreter as ```virutalenv -p <path of python 3.6 /3.7> <name_of_virtual_env>```. Incase you don't have virtualenv install it using ```sudo pip3 install -U virtualenv```.
* check the pip version (pip>0.19). Incase lower version, upgrade the pip version using ```pip install --upgrade pip```.

#### Create a virtual env using __Anaconda__ (Ubuntu)
* Install Anaconda, if not installed in your system from [**(Conda)**](https://www.anaconda.com/products/individual).
* After successful installation run ``` conda create -n <name_of_virtual_env> ```. Add/Update the version of python in conda path,
version supported (3.6 - 3.7).

### Install Rasa
``` $ pip install rasa ```

### Setup astroX bot :rocket:
Clone the repository for astroX bot

``` 
$ git clone https://github.com/Shandilya21/astroX.git
$ cd astroX
$ pip install -r requirement.txt
```

#### Rasa Server
To run the astroX bot and begins the exciting space adventures, fast you seat belt and run

``` rasa run --enable-api --cors '*' ```

#### Rasa Action Server

``` rasa run actions --actions actions ```

#### Credentials and Deployment
* Incase of using credentials (host on faceboo messenger, slack, etc.) please follow the Rasa Official [(Docs)](https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels/)

* For deploying this Rasa Assistant, you can use one line deployment script that install Kubernetes cluster on your machine with sensible defaults. For more in details, search teh Rasa official [(Docs)](https://rasa.com/docs/rasa/user-guide/how-to-deploy/)

``` curl -s get-rasa-x.rasa.com | sudo bash ```

#### References

* Rasa [(Docs)](https://rasa.com/docs/rasa/)

### Contributing

Contributions are very welcome. If you know how to make this code better, please open an issue. If you want to submit a pull request, please open an issue first.

### TODO
* Add more data related to space science.
* Add quiz session related to outer space.
