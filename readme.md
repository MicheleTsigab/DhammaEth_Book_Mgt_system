
<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/micheletsigab/DhammaEth_Book_Mgt_system">
    <img src="core/static/img/dhamma.gif" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Dhamma Ethiopia Library Management</h3>

  <p align="center">
    An app that helps manage book inventory.
    <br />
    <a href="readme.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/micheletsigab/DhammaEth_Book_Mgt_system">View Demo</a> -->
    ·
    <a href="https://github.com/micheletsigab//issues">Report Bug</a>
    ·
    <a href="https://github.com/micheletsigab/DhammaEth_Book_Mgt_system/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Book Filter][Book-filter-screenshot]](Documentation/images/filter_books.png)

This project is intended to be used by a librarian clerk to manage books with a simple UI to allow them to lend,see returned books as well as add Members for whom it can be lent.

In addition to that this app:
* has a detailed filter functionality that allow for simple retrieval of borrowed books.
* is also highly extensible, to add more features.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Django
* HTMX
* Pillow
* Django-filters
* django-crispy-forms
* django-widget-tweaks
* Bootstrap
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

There are two ways you can setup this project.1. using the dockerfile 2. using pip

### Prerequisites


* All prerequistes are in the requirements.txt

### Installation

#### Using dockerfile
1. Clone the repo
   ```sh
   git clone https://github.com/micheletsigab/DhammaEth_Book_Mgt_system.git
   ```
3. change WORKDIR in `dockerfile` to the root directory of the cloned project (besides manage.py)
4. Change volume in `docker-compose.yml` as well to to the root directory of the cloned project (i.e besides manage.py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

#### using pip
 Run
  ```sh
  pip install -r requirements.txt
  ```
 ```sh 
 manage.py make migrations 
 ```

 ```sh 
 manage.py migrate
 ``` 
<!-- USAGE EXAMPLES -->
## Usage

[![Add Book][Book-add-screenshot]](Documentation/images/add_book.png)

[![Add Author][Book-add-screenshot]](Documentation/images/add_author.png)

1. run 
```sh
manage.py createsuperuser
```
2. go to 0.0.0.0:8000/admin(or whereever hosted) and create a user for the list of librarian clerks
3. Go to 0.0.0.0:8000/accounts/login and have fun.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add a nice UI to detail and list page
- [ ] Add searchable and autocomplete data list in bookfields
- [ ] implement HTMX to sidebar to add more interactivity features.
- [ ] Multi-language Support
    - [ ] Amharic


See the [open issues](https://github.com/micheletsigab/DhammaEth_Book_Mgt_system/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
This is part of my volunteer work for Dhamma Ethiopia. I would appreciate any contribution.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `license.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michele Tsigab - [LinkedIn](https://linkedin.com/in/micheletsigab) - micheletsigab@gmail.com

Project Link: [https://github.com/micheletsigab/DhammaEth_Book_Mgt_system](https://github.com/micheletsigab/DhammaEth_Book_Mgt_system)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments -->
<p align="right">(<a href="#readme-top">back to top</a>)</p>
