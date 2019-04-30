* CI Status [![CircleCI](https://circleci.com/gh/comp3300-comp9900-term-1-2019/capstone-project-czhx/tree/master.svg?style=svg&circle-token=9be1f23acc11a415ea9e838befe141e5419106dd)](https://circleci.com/gh/comp3300-comp9900-term-1-2019/capstone-project-czhx/tree/master)

* Frontend: [gobo](https://gobo.cfapps.io)
* Backend: [gobo-api](https://gobo-api.cfapps.io/v1/help)

# Intro
GoBo is a web-based student life assistant, which creates a more enjoyable living and studying environment for CSE students, by supporting them with a knowledge base including course details, enrollment suggestions, and other useful information.

# Deploy Instruction

## CircleCI
We have configured workflow on CircleCI. To deploy our applications, just make a simple commit to this branch, or click the CI status badge above to access the Circle dashboard.

## Manual Deployment

### Frontend

Requirements:
* node: ^10.15.1
* cf-cli (https://docs.cloudfoundry.org/cf-cli/install-go-cli.html)

1. Test and Build
```
$ cd czhx-web
$ yarn && yarn test && yarn build
```
2. Deploy
First login to CloudFoundry.
Note the login credentials are configured as environment variables on CircleCI, you can find them through this link: https://circleci.com/gh/comp3300-comp9900-term-1-2019/capstone-project-czhx/edit#env-vars.
```
$ cf login cf login --skip-ssl-validation -a api.run.pivotal.io -u $CF_USER -p $CF_PASSWORD -o unsw-comp9900-19t1-czhx -s development
```
Then you can push the application with the config file `manifest.yml`.
```
$ cf push -f manifest-pws.yml && cf logout
```

### Backend

Requirements:
* cf-cli

For backend we don't have to build the application, just go through a similar deploy process.
First login to CloudFoundry.
Note the login credentials are configured as environment variables on CircleCI, you can find them through this link: https://circleci.com/gh/comp3300-comp9900-term-1-2019/capstone-project-czhx/edit#env-vars.
```
$ cd backend
$ cf login cf login --skip-ssl-validation -a api.run.pivotal.io -u $CF_USER -p $CF_PASSWORD -o unsw-comp9900-19t1-czhx -s development
```
Then you can push the application with the config file `manifest.yml`.
```
$ cf push -f manifest-pws.yml && cf logout
```
