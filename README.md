![Helio RC](https://raw.githubusercontent.com/heliorc/imuf-release/master/final.svg)
# IMUF Official Releases

Hex releases for supported firmware.

# UPDATE

We have decoupled the updating of the flight code firmware from the update process for the IMU-F unit. When there is an update to IMU-F, you will want to use the tool provided to update IMU-F. We will no longer be creating additional aggregates since it is no longer neccesary to do so. This should make things more clear as to what is happening when you update. You will only need to update IMU-F when there is a new version specifically for IMU-F and deprecates the "iumufupdate" command in the CLI that came with our gyro driver in BxF/iNav.


The hexes are aggregates of the firmware plus any updates to our IMUF code. They are concatenated into an aggregate using the provided concat.py script. See https://github.com/betaflight/betaflight/blob/master/LICENSE lines 235-243.


```
A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.
```

<p>See https://github.com/heliorc/imuf-release/tree/legacy for old firmware releases</p>
<p>See https://www.heliorc.com/wiring for how to hook up the HELIO SPRING.</p>
<p>See https://www.heliorc.com/docs for more information on settings.</p>

<p>See https://github.com/heliorc/imuf-release-bef for Betaflight releases.</p>
<p>See https://github.com/heliorc/imuf-release-inav for iNav releases.</p>
