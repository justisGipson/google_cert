# Introduction to Git and GitHub - Week 4

## Collaboration

### Pull Requests

**Forking** is a way of creating a copy of the given repository so that it belongs to our user.

**Pull request** is a commit or series of commits that you send to the owner of the repository so that they incorporate it into their tree.

When collaborating on projects hosted on GitHub, the typical workflows is:

1. Create a fork of the repo
2. Work on that local fork

* [More Fork and Pull Request Info](https://help.github.com/en/articles/about-pull-request-merges)

---

## Code Review

### Managing Collaboration

**Code review** means going through someone else's code, documentation or configuration and checking that it all makes sense and follows the expected patterns.

The goal of a code review is:

* To improve the project by making sure that changes are high quality
* Helps make the contents are easy to understand
* The style is consistent with the overall project
* Remind us about any important cases

* Increases the number of eyes on the code - reducing the number of bugs and increase code quality
* Not about us being goo/bad coders but making our code better

#### Extras

* [Google Style Guide](http://google.github.io/styleguide/)
* [Pull Requests and Review](https://help.github.com/en/articles/about-pull-request-reviews)
* [Perfect Code Reviews](https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31)
* [What is a Code Review?](https://smartbear.com/learn/code-review/what-is-code-review/)

---

### Managing Projects

When collaborating:

* Documenting any work is important
* As a project maintainer, reply promptly to pull requests and don't let them stagnate
* Understand any accepted changes
* Use an issue tracker to coordinating who does what and when
* Have a way of communicating and coordinating between contributors

### Continuous Integration

**Continuous integration** is a system building and testing code every time there's a change.

**Continuous deployment** means the new code is deployed often. The goal is to avoid roll outs with a lot of changes between two versions of a project and instead do incremental updates with only a few changes at a time.

Some of concepts that needs to be dealt with when creating CI/CD includes:

1. Pipelines, which specifies the steps that need to run to get the desired result
2. Artifacts, which is the name used to describe any files that are generated as part of the pipeline

#### Extras

* [Open Source Ethics](https://arp242.net/diy.html) 
* [Closing Issues with Keywords](https://help.github.com/en/articles/closing-issues-using-keywords)
* [Repo Contribution Guidelines](https://help.github.com/en/articles/setting-guidelines-for-repository-contributors) 
* [What is CI/CD](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html)
* [Getting CI/CD Right](https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/)
* [Travis-CI Tutorial](https://docs.travis-ci.com/user/tutorial/)
* [Travis-CI Build Stages](https://docs.travis-ci.com/user/build-stages/)
---
