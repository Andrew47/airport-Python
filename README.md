The Airport Challenge in Python
==============================

This is a solution to Makers Academy's [Airport Challenge](https://github.com/makersacademy/airport_challenge). The original
was written in Ruby, and can be found  [here](https://github.com/Andrew47/airport_challenge). There is also a version in
[JavaScript](https://github.com/Andrew47/airport_JS)

This solution uses a test-driven approach, with feature and unit tests
implemented using the [unittest](https://docs.python.org/2/library/unittest.html) library.

##Installation notes

The program was written having installed the [Anaconda](https://www.continuum.io/downloads) Python distribution. Python version 2.7.11 was used.

First a new environment should be created:

`$ conda create --name snowflakes mock`

This creates an environment called 'snowflakes', with the mock package installed.

To activate this environment:

* In Linux, OS X:  `$ source activate snowflakes`
* In Windows: `$ activate snowflakes`

To deactivate:

* In Linux, OS X: `$ source deactivate`
* In Windows: `$ deactivate`

More information about environments can be found [here](http://conda.pydata.org/docs/using/envs.html).

Then, the repository should be cloned and the directory changed into:

```
$ git clone git@github.com:Andrew47/airport-Python.git
$ cd airport-Python
```

##Using the program

Open the python interpreter and import the modules:

```
$ python
>>> from app.airport import Airport
>>> from app.plane import Plane
```

Then an airport can be created by typing `airport = Airport()` and a plane by typing
`plane = Plane()` in the command line.

The plane can land at the airport (`plane.land(airport)`) and can take off (`plane.take_off(airport)`). Weather is randomly generated each time the plane
seeks to take off or to land. Stormy weather prevents take off or landing.

If `plane.is_airborne` returns `True`, the plane is in the air. If `plane.is_airborne`
returns `False`, the plane has landed.

The default airport capacity is 20. However, a new airport (airport1000) can be created
with this default overridden (`airport1000 = Airport(1000)`). Planes cannot be landed at
a full airport (`airport.is_full()` returns True). 

##User Stories being met
```
As an air traffic controller
So I can get passengers to a destination
I want to instruct a plane to land at an airport and confirm that it has landed

As an air traffic controller
So I can get passengers on the way to their destination
I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport

As an air traffic controller
To ensure safety
I want to prevent takeoff when weather is stormy

As an air traffic controller
To ensure safety
I want to prevent landing when weather is stormy

As an air traffic controller
To ensure safety
I want to prevent landing when the airport is full

As the system designer
So that the software can be used for many different airports
I would like a default airport capacity that can be overridden as appropriate
```

##Author
* [Andrew Burnie](https://github.com/Andrew47)
