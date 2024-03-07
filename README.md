# dnsx_filtre_mix_subdomains

This program works with dnsx. please use with only linux os

```
https://github.com/projectdiscovery/dnsx
```


It is used to resolve subdomain names with the dnsx program. The -wd parameter along with dnsx is used to filter wildcard subdomains in your subdomain list. If your subdomain list has more than one different domain name, you must have more than one domain address that you can use with the -wd parameter.

example subdomain list:
-----------------------

```
paypal.com
www.paypal.com
xxx.paypal.com
```

If you have a list called subdomains.txt belonging to a single domain as above, you can only use paypal.com with the -wd parameter.

```
dnsx -l subdomains.txt -wd paypal.com -a -cname
```

The logic here is that wildcard subdomains in the subdomains.txt file are cleared according to the domain address you specify with the -wd parameter.
But if you have a subdomains.txt file like the one below, which domain will you use with the -wd parameter?

example mix subdomain list:
---------------------------

```
www.facebook.com
asset.facebook.com
www.shopify.com
yyy.shopify.com
xxx.xxx.shopify.com
paypal.com
www.paypal.com
xxx.paypal.com
```

If you have such a subdomains.txt file, you must use more than one domain address with the -wd parameter.This is exactly why I made the dnsx_filtre_mix_subdomains.py program.
This program is designed to automatically use all domain addresses in a subdomains.txt file with the -wd parameter.

Another good thing is that if the -wd parameter "paypal.com" is used with the subdomains.txt file, all paypal.com subdomains in subdomains.txt are transferred to another list and then the wildcard cleaning process is started with DNSX. In this way, subdomains in the subdomains.txt file that do not belong to paypal.com are not scanned every time and no time is wasted. After the scan for paypal.com is completed, it uses another domain address in the list with the -wd parameter and continues the process of cleaning wildcard subdomains.

install:
--------

```
pip3 install -r requirements.txt
```

usage:
-----

```
#Before running this program, the dnsx program must be installed on your computer.
#You don't have to use the --output parameter. If you do not use this parameter, you will get an output named final_subdomains.txt by default.

python3 dnsx_filtre_mix_subdomains.py --list subdomains.txt --output results.txt
```
