![travis-ci](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)

# Alice Pi
Code for Alice's remote Pis

## Installation
* `pip install alice_pi`

## Gotchas
* Don't forget that we have to do this: `echo "dtoverlay=w1-gpio" >> /boot/config.txt` (already in the fabfile) to get the 1-wire to work.

