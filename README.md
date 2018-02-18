## Donation :dollar: :euro: :pound: :yen:

<img src="https://github.com/webcyou/crypto-currency-icon/blob/master/design/images/default/1.png" width="15" height="15"/>  Donate **Bitcoin** to this address:
```cpp
3AQQg87vY31RPCKRrDrkHQijP9nsVY7mtb
```

<img src="https://github.com/webcyou/crypto-currency-icon/blob/master/design/images/default/3.png" width="15" height="15"/>  Donate **Ethereum** to this address:
```cpp
0xc5b82006d2aba5269d2f8ca6d1dc81d3331c3c02
```

## Screenshot
Here is screenshot of info when running once:

![Screenshot of info when running once](https://user-images.githubusercontent.com/9158844/36348577-7e96893a-1483-11e8-970f-f35df4ae71a0.png)

## Usage

### :penguin: Ubuntu 16.04

First, we need to install its dependencies, (if you don't have pip3, do `sudo apt install python3-pip`):

```bash
sudo -H pip3 install colorclass terminaltables
```

Clone this repository to your home directory or wherever you want:

```bash
$ cd ~ && git clone https://github.com/cosmicog/miningpoolhub_info
```

Go to [Mining Pool Hub - Edit Account](https://miningpoolhub.com/?page=account&action=edit) page and copy your api key, and paste it into `api_key.txt` file in this repository with your favourite editor.

And run the single one by:

```bash
$ python3 display_once.py -a PASTE_YOUR_API_KEY_HERE
```

Or run with your extra favourite currency (TRY below):

```bash
$ python3 display_once.py -a PASTE_YOUR_API_KEY_HERE -f TRY
```

Or continuous one:

```bash
Coming soon...
```
Here is all options:
```bash
$ python3 display_once.py --help
usage: display_once.py [-h] -a api_key [-i id] [-c crypto_currency]
                       [-f fiat_currency]

  -h, --help          show this help message and exit
  -a api_key          API KEY from 'Edit Account' page
  -i id               USER ID from 'Edit Account' page
  -c crypto_currency  Which exchange currency to display total in (default
                      BTC)
  -f fiat_currency    Not needed, extra column for displaying other fiat
                      currency total (default TRY)
```

<br> 

### :shit: Windows 10

_Coming soon._ If you aren't python developer, you can start by [this](http://lmgtfy.com/?iie=1&q=python+hello+world+windows) :trollface: 



