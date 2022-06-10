# **ACME Payment System**

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This is an app to calculate amount of payment for employees. The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following information:

### **Monday - Friday**
* 00:01 - 09:00 25 USD
* 09:01 - 18:00 15 USD
* 18:01 - 00:00 20 USD

### **Saturday and Sunday**
* 00:01 - 09:00 30 USD
* 09:01 - 18:00 20 USD
* 18:01 - 00:00 25 USD

The goal of this application is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

* **MO**: Monday
* **TU**: Tuesday
* **WE**: Wednesday
* **TH**: Thursday
* **FR**: Friday
* **SA**: Saturday
* **SU**: Sunday

<!-- GETTING STARTED -->
## Getting Started
Next you will read about software requirements as well as how you can install this application

### Prerequisites
This script was coded with:
* Python 3.6.10
* There is no dependency requeriments

### Installation
Follow the instructions below
1. Create the environment
```sh
   virtualenv env
   source env/bin/activate
   ```
2. Clone the repo
```sh
   git clone https://github.com/3rickfs/Acme-Payment-System.git
   ```

<!-- USAGE -->
## Usage
To run the app use the following command
```sh
   cd app/
   python acme_payment_cli.py --txtinput [txt_input_file_path]
   ```
* _[txt_input_file_path]_ is a .txt file including the employee's name, day and time information. The format is as follows: [NAME]=[DAY1][HH1]:[MM1]-[HH2]:[MM2],[DAY2][HH1]:[MM1]-[HH2]:[MM2],...
* Day abbreviations are explained above.
* Beginnig time: [HH1]:[MM1]; Ending time: [HH2]:[MM2]

### Test cases:
To run tests cases **input_1** and **input_2** variables in _tdd_script.py_ must be updated according to the path in your machine
* RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
* ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
* DIANA=MO10:00-12:00,TU10:00-12:00,WE10:00-12:00,TH01:00-03:00,FR10:00-12:00,SA14:00-18:00,SU20:00-21:00
* KARL=MO07:00-12:00,TU10:00-12:00,WE10:00-12:00,TH01:00-03:00,FR10:00-12:00,SA14:00-18:00,SU20:00-21:00
* MARK=MO07:00-12:00,TU01:00-23:00,WE10:00-12:00,TH01:00-03:00,FR10:00-12:00,SA14:00-18:00,SU20:00-21:00
* AMELIA=MO07:00-12:00,TU01:00-23:00,WE10:00-12:00,TH01:00-03:00,FR10:00-12:00,SA14:00-18:00,SU01:00-23:00

To run tests use the following commands
```sh
   cd tdd_tests/
   python tdd_script.py
   ```

<!-- ROADMAP -->
## Roadmap

- [x] Calculate employee's payment according to days and time of work
- [x] Considering overtime work. Example: started at 7:00 and finished at 20:00 hours.
- [ ] Validate correct format of txt input file.
- [ ] Include rest hours.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>