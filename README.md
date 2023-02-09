# contact-us

## What does it do?

`contact-us` is a microservice to handle contact form requests.

E.g: You have a contact form in your website and you need some backend code to actually receive the request and send you the message via email or other means. `contact-us` is the standalone solution for you.

## How does it do it?

`contact-us` provides an API for sending information such as email, name, phone, message body and then transmits these messages via email (or any other means)

## Instalation

As of this point in time, installation from source is the only option. The plan is to release it as a python package and also provide a docker image.

### Instalation from source

```
git clone https://github.com/gtsop/contact-us.git
cd contact-us
pip install .
```

## Configuration

### Storage

The default configuration option uses an in-memory database which won't be a reasonable option for production, but helps you validate the application has been installed succesfully.

`contact-us` is tested to be working with `sqlite`. In order to configure a permanent storage file provide this environment variable:

```
export STORAGE_DB_URI="sqlite:///.local.db"
```

## CLI usage

A quick way to test the workings of this application is to use it's cli, for instance try this:

```
contact-us create-message foo@bar.com "hello world"
contact-us list-messages
contact-us create-message bar@baz.com "goodbye world"
contact-us list-messages
contact-us send-message 2
contact-us list-messages
```