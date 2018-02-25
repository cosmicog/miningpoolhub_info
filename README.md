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

Or run with your extra favourite currency, for example **EUR**, **GBP**, **JPY** etc. (**TRY below**):

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

If you aren't python developer, you can start by [this](http://lmgtfy.com/?iie=1&q=python+hello+world+windows) :trollface: 

<br>

## Donations :dollar: :euro: :pound: :yen:

Donate <img src="https://raw.githubusercontent.com/zcash/logos/master/yellow-zcash-logo.png" width="15" height="15"/> **Zcash** to this address:
```
t1R7hecCF2kfiRVrEtnrUJZr57zKqDKRpvt
```
![zcash](https://user-images.githubusercontent.com/9158844/36625316-3c14cba8-192e-11e8-9c2d-3855fda623b7.png)
<img src="https://raw.githubusercontent.com/zcash/logos/master/yellow-zcash-logo.png" width="60" height="60"/>
---

<br><br>

Donate <img src="https://github.com/webcyou/crypto-currency-icon/blob/master/design/images/default/1.png" width="15" height="15"/> **Bitcoin** to this address:

```
3AQQg87vY31RPCKRrDrkHQijP9nsVY7mtb
```
![bitcoin](https://user-images.githubusercontent.com/9158844/36625315-3bf470ec-192e-11e8-8dc4-e8ea15b00a6f.png)
<img src="https://github.com/webcyou/crypto-currency-icon/blob/master/design/images/default/1.png" width="60" height="60"/>
---

<br><br>

Donate <img src="https://github.com/webcyou/crypto-currency-icon/blob/master/design/images/default/3.png" width="15" height="15"/> **Ethereum** to this address:

```
0xc5b82006d2aba5269d2f8ca6d1dc81d3331c3c02
```
![ethereum](https://user-images.githubusercontent.com/9158844/36625314-3bd89dd6-192e-11e8-984d-a1e61c4a0ffa.png)
<img src="https://github.com/webcyou/crypto-currency-icon/blob/master/design/images/default/3.png" width="60" height="60"/> 
---
