## Soya 

<img src="icon.jpg" alt="soya" width="250px" />


__Soya__ is a bundle of __Web APIs__, which implemented by [__Flask__](https://github.com/mitsuhiko/flask)

As a further development based on __Baidu vehicle network APIs__, __Soya__ is designed to reduce the complexity
of accessing the Baidu vehicle network service. It's a bridge between the service and the terminal device, like
an Andriod smartphone.

__Things worth to be mentioned__:

* Hide the detail of the authentication with __Baidu__ vehicle service;

* Provide new access and result serialization mechanisms(__more configable__) with terminal devices;

* More flexible __validation of input parameters__, and more friendly __handle of exceptions__;


## Quick Start

### Installation

Install as developer

```
$ make develop
```

Install as package

```
$ make install
```

More options

```
$ make help
```

### Development

Run server, suppose that you put the package to your home directory:

```
$ cd ~/soya/soya
```

then simply run:

```
$ python server
```

## Documentation 

[__Soya API Documentation__](https://github.com/streethacker/soya/blob/develop/doc/documentation.md)
