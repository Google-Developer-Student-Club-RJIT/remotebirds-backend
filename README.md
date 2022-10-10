# Remote Birds (Backend)

<div align="center">

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend)&nbsp;
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat&logo=github)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend)&nbsp;
![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=brightgreen&style=flat&logo=github)&nbsp;
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend)&nbsp;
[![GitHub stars](https://img.shields.io/github/stars/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/network/members)
[![GitHub Contributers](https://img.shields.io/github/contributors/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/pulls)
[![GitHub closed-issues](https://img.shields.io/github/issues-closed-raw/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/pulls)
[![GitHub closed-prs](https://img.shields.io/github/issues-pr-closed-raw/Google-Developer-Student-Club-RJIT/remotebirds-backend)](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/pulls)

</div>

## Tech-Stack

<br>

![Django](https://img.shields.io/badge/-Django-092E20?style=plastic&logo=Django)
![Python](https://img.shields.io/badge/-Python-8fcfd1?style=plastic&logo=Python)

## About the Project

This is the backend or API of the Remotebird jobs project. This project is a part of the Hacktoberfest on behalf of Google Developer Student Club's RJIT. The project is made using Django and Python.

This API can be integrated anywhere whether it is a website(with any frontend Frameworks) or an app. This API is made to provide the user with the latest jobs that are posted on twitter. The user can also search for the jobs according to their requirements.

The API is hosted on Heroku and can be accessed using the following link:
https://remotebirdjobs-api.herokuapp.com/

The onlyendpoint that is available is the search endpoint. The search endpoint can be accessed using the postman collection that is provided in the repository. Or you can use the following link: https://www.getpostman.com/collections/f89b1d05d20d74d886ff

## Getting Started

The complete project is Dockerized. To run the project you can follow following steps:

```
docker-compose build
docker-compose up
```

Or you can simply run the following command to run the project after cloning the project:
Install virtualenv then create a virtual environment venv:
```
pip3 install virtualenv
virtualenv venv
```
activate virtualenv using following command in Mac/Linux:

```
source venv/bin/activate
```
in windows:
```
venv\Scripts\activate
```

Then install all the dependencies using:
```
pip3 install -r requirements.txt
```
And run:
```
python manage.py runserver
```

To test the exsisting api please follow the following postman collection:
https://www.getpostman.com/collections/f89b1d05d20d74d886ff

## 📌Contributing Guidelines :
<br>
<h3>First read CONTRIBUTING.md</h3>

### Do not make a PR without getting the issues assigned. Read Rules Carefully!

*1.* Fork [this](https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend) repository.

*2.* Clone your forked copy of the project.

```
git clone https://github.com/<your_name>/remotebirds-backend.git
```

*3.* Navigate to the project directory :file_folder: .

```
cd remotebirds-backend
```

*4.* Add a reference(remote) to the original repository.

```
git remote add upstream https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend.git
```

*5.* Check the remotes for this repository.

```
git remote -v
```

*6.* Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).

```
git pull upstream main
```

*7.* Create a new branch.

```
git checkout -b <your_branch_name>
```

*8.* Perfom your desired changes to the code base and track your changes:heavy_check_mark: .

```
git add .
```

*9.* Commit your changes .

```
git commit -m "Relevant message"
```

*10.* Push the committed changes in your feature branch to your remote repo.

```
git push -u origin <your_branch_name>
```

*11.* To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repo you are suppose to make a PR to.

*12.* Add appropriate title and description to your pull request explaining your changes and efforts done. Always make sure you have pulled the latest code from the main branch before making a PR.

*13.* Click on `Create Pull Request`.

*14.* Hurray ❗ You have created a PR to the remotebirds-backend 💥 . Sit back patiently and relax till then the project maintainers will review your PR. Please understand, there will be some time taken to review a PR and can vary from a few hours to a few days too so be patient and keep contributing.


### Our Contributors

<a href="https://github.com/Google-Developer-Student-Club-RJIT/remotebirds-backend/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Google-Developer-Student-Club-RJIT/remotebirds-backend" />
</a>





