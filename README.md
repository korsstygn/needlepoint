[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10802036.svg)](https://doi.org/10.5281/zenodo.10802036)

# gh-pages-about-me

## About the Repository
This repository contains a public GitHub Template, designed as a sandbox environment for students who want to learn how to publish simple, static websites using [GitHub Pages](https://pages.github.com). 

To learn more about how to use this template, please visit our [wiki](https://github.com/SSLIS/gh-pages-about-me/wiki), and follow the instructions. For more information, you can check out my video lecture on [Publishing Web Content with GitHub Pages](https://play.hb.se/media/0_5agfo9py). While that video was recorded before I designed this repository, and therefore does not reference it yet, the lecture follows a very similar procedure and should answer most of your questions.

These instructions do not require any previous knowledge about `git` or GitHub, but do assume that you have an active GitHub Account, and that you have downloaded the [GitHub Desktop](https://desktop.github.com/) software. A very basic knowledge of `HTML` and `CSS` is also useful.

For a low-threshold introduction to git and GitHub, including a quick introduction to this repository, a live run-through of some of the commands of your basic git and GitHub workflows, and definitions of concepts like fork, commit, push, and pull request be sure to check out [my pizzaParty repository](https://github.com/SSLIS/pizzaParty), and [its accompanying video lecture](https://play.hb.se/media/0_mvgov641).

## A Note on Using the Template
This template contains a series of files that are important for archiving purposes, and for upholding community standards, such as our [code of conduct](CODE_OF_CONDUCT.md), [contribution instructions](CONTRIBUTING.md), [license information](LICENSE), and [Zenodo JSON metadata](.zenodo.json). While these files are useful to contextualize this specific repository, they would be irrelevant (or even contain false information) when copied over into the user's own repository. (For example: the [license](LICENSE) would identify me as the copyright holder of your repository, and the [code of conduct](CODE_OF_CONDUCT.md) would similarly identify me as a point of contact regarding your repository.)

To resolve this issue, the template uses GitHub Actions to delete some irrelevant files (and modify others). This happens **after** the user creates their own copy of the repository, and results in a subsequent bot-made `commit`, that cleans up the template. Where, initially, your repository will look exactly like this one (including the [license](LICENSE) etc.), these superfluous files will disapear when the process is finished. 

This process takes some time, albeit usually less than a minute. You may need to refresh your page to see it take effect. You will notice that the process was succesful when a number of files have been removed from your repository, and this README.md file instead contains some dummy text.

I would recommend that you wait until this process is finished (which should not take long) before cloning your repository to your local machine, and starting to modify it. If you do not notice any changes after some time, remember to refresh your page. You can also always go and check if the process is still running (and if anything has gone wrong) by navigating to the `Actions` tab at the top of your repository's page.

## Credits
This repository was originally developed by [Wout Dillen](https://github.com/WoutDLN) as a teaching tool in the Digitising Cultural Heritage Materials course at the [University of Borås](https://www.hb.se/), where he currently works as a Senior Lecturer in Library and Information Science. Continued development of the template has in part been made possible by [Huminfra](https://www.huminfra.se), the Swedish national infrastructure project for Digital Humanities.

Special thanks to [vincerubinetti](https://github.com/vincerubinetti), whose GitHub Action (mentioned in [this forum comment](https://github.com/orgs/community/discussions/22183#discussioncomment-4585507)) formed the basis of the template cleanup procedure mentioned above, and to [Andre601](https://github.com/Andre601), for helping me figure out how to update the `.yml` file to get it to work.
