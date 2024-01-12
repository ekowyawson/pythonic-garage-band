# Lab: Class 04

## Project: Pythonic Garage Band

**Author**: Ekow Yawson
**Version**: 1.0.0

### Links and Resources

---

- [In Tests We Trust - TDD with Python](https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932)

### Setup

---

**Requirements:**

- Install **pytest**: run `pip3 install pytest`

**Tests:**

- To run all tests, run the following command at the root of the project:

```bash
python -m pytest

# Or, if you are in a virtual env i.e., venv:
pytest
```

### Overview

---

This is a program which uses Python classes to model a Band made up of different types of musicians
for example: Guitarist, Bassist, Drummer, etc. We will use Python classes to model a Band made up of
different kinds of musicians.

### Feature Tasks and Requirements

---

- [x] Start with **Guitarist**, **Bassist**, and **Drummer**.
- [x] Use a **Musician** base class to handle common functionality with which certain types of musicians will inherit.
- [x] Make you code pass the supplied unit tests.
  - Do NOT modify the supplied tests (except to enable for stretch goals.)

#### Band Tests

- [x] A Band instance should have a **name** attribute which is a **string**.
- [x] A Band instance should have a **members** attribute which is a **list of instances** that inherit from **Musician** base (or super) class.
- [x] A Band instance should have a **play_solos** method that asks each member musician to play a solo, in the order they were added to band.
- [x] A Band instance should have appropriate **__str__** and **__repr__** methods.
- [x] A Band should have a class method **to_list** which returns a list of previously created Band instances

#### Musician Subclass Tests

- [x] Each kind of Musician instance should have appropriate **__str__** and **__repr__** methods.
- [x] Each kind of Musician instance should have a **get_instrument** method that returns **string**.
- [x] Each kind of Musician instance should have a **play_solo** method that returns **string**.

#### Stretch

- See tests marked **“stretch”** in supplied test suite.
- [x] Make Musician **“abstract”** - aka an _Abstract Base Class_
- [ ] Add your own tests.
