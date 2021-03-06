# Census2Ged
Like this project? Send a couple dollars my way and/or visit my blog to see what else I'm up to!
- [Paypal](https://www.paypal.me/ReneeSchmidt)
- [Blog](https://famgenealogy.blogspot.com/)
## Purpose
Converts census transcriptions and household examinations made in [Genscriber](http://www.genscriber.com/genapps/) to gedcom files. You can see some of my posts about Census2Ged [here](https://famgenealogy.blogspot.com/p/my-programs.html)

## Screenshots
![Screenshot of Census2Ged](https://raw.githubusercontent.com/xXReneeXx/Census2Ged/master/screenshot2.PNG)

## Character Encoding
Currently only the Swedish Household Examination part of the program includes support for **utf-8**, however I hope to change this in the future so all parts of the program support it.

All gedcoms (regardless of country) are identified as **utf-8** encoded in the **header**.

## Default Tags
Census2Ged picks out gedcom 5.5.1 compliant tags for each piece of information for you, however you may wish to change these (they will still be gedcom 5.5.1 compliant, but they will use EVEN and TYPE tags instead).

### English Census Tags

| Option Name      | Default Tag | Suggested Tag         |
|------------------|-------------|-----------------------|
| Immigration Year | IMMI        | Don't Change          |
| Occupation       | OCCU        | Don't Change          |
| Race             | DSCR        | Race                  |
| Naturalization   | NATU        | Naturalization Status |
| Literacy         | EDUC        | Literacy              |
| Children Born    | DSCR        | Number of Children    |
| Language         | DSCR        | Language              |
| Military         | DSCR        | Military              |
| Disability       | DSCR        | Disability            |
| Property         | PROP        | Don't Change          |

### Swedish Household Examination Tags

| Option Name            | Default Tag | Suggested Tag         |
|------------------------|-------------|-----------------------|
| Occupation             | OCCU        | Don't Change          |
| Communion              | ORDI        | Don't Change          |
| Examination            | ORDI        | Don't Change          |
| Moving In Records      | IMMI        | Don't Change          |
| Moving Out Records     | IMMI        | Don't Change          |
| Death                  | DEAT        | Don't Change          |



## Handling of Custom Tags
The program handles custom tags as recommended in the Gedcom 5.5.1 standard. This will allow them to be compatible with virtually every genealogy program available.

The following is the format the program writes these custom tags in. It uses an 'EVEN' (event) tag, then modifies it with a 'TYPE' tag.

```
1 EVEN description of event
2 TYPE new tag name
```
## Handling of Dates, Years, and Ages

### English Censuses
Approximate birth dates are calculated using the year of the census - age of the person at the time if the birth date is not explicitly specified. If the age of a person is a fraction it is changed to 0. Year of the census is attached to all of the applicable facts.

### Swedish Household Examinations
Assumes a date structures which fit either of the following

```
dd/mm yyyy
dd/m yyyy
d/mm yyyy
d/m yyyy

dd/mm yy
dd/m yy
d/mm yy
d/m yy

```
for instance, the date March 7, 1867 could be written in the following ways:
```
07/03 1867
07/3 1867
7/03 1867
7/3 1867

07/03 67
07/3 67
7/03 67
7/3 67
```
## Supported Relationship Types
The United States section supports the following relationship types:
- Head
- Wife
- Son
- Daughter
- Child

The Swedish Section Supports the following relationship types:
- Head
	- far, pappa, fader, man, husfader, enkl., enkeman, änkl., änkling, eg., egare, ägare
- Wife Married to head
	- mamma, mor,moder, hustru, fru, maka, enka, enk.,husmoder, änka, änk., d.h., desshustru, dess hustru, h.
- Children
	- barn, son, dotter, d., dtr., s.
- Illegitimate Children (Puts these children in their own family for the sake of clarity)
	- antenuptius, ante nuptius, a.n., oä., oäkta

## Types of Data (Supported and Unsupported) For Each Census
The goal is to eventually present every piece of information in some way for every census. I have copied the names of each of the fields from the [IPUMS enumeration forms](https://usa.ipums.org/usa/voliii/tEnumForm.shtml)

## United States Censuses 
### 1910 Census

**LOCATION:
STREET, AVENUE, ROAD, ETC.
HOUSE NUMBER (IN CITIES AND TOWNS)**

- [X] Number of dwelling in order of visitation
- [X] Number of family, in order of visitation
- [X] Name of each person whose place of abode on April 15, 1910, was in this family. Enter surname first, then the given name and middle initial, if any. Include every person living on April 15, 1910. Omit children born since April 15, 1910
- [X] Relationship of this person to the head of the family

**PERSONAL DESCRIPTION:**

- [X] Sex
- [X] Color or Race
- [X] Age at last birthday (partially supported through calculation of aprox. date of birth)
- [ ] Whether single, married, widowed, or divorced
- [X] Number of years of present marriage (partially supported through calculation of aprox. date of marriage)
- [X] Mother of how many children, Number born, Number now living

**NATIVITY:
PLACE OF BIRTH OF EACH PERSON AND PARENTS OF EACH PERSON ENUMERATED. IF BORN IN THE UNITED STATES, GIVE THE STATE OR TERRITORY. IF OF FOREIGN BIRTH, GIVE THE COUNTRY**

- [X] Place of birth of this person
- [ ] Place of birth of father of this person
- [ ] Place of birth of mother of this person

**CITIZENSHIP**

- [X] Year of immigration to the United States
- [X] Whether naturalized or alien
- [X] Whether able to speak English; or, if not, give language spoken

**OCCUPATION:**

- [X] Trade or profession of, or particular kind of work done by this person, as spinner, salesman, laborer, etc.
- [X] General nature of industry, business, or establishment in which this person works, as cotton mill, dry goods store, farm, etc.
- [ ] Whether an employer, employee, or working on own account.

**IF AN EMPLOYEE:**

- [ ] Whether out of work on April 15, 1910
- [ ] Number of weeks out of work during year 1909

**EDUCATION:**

- [X] Whether able to read, Whether able to write
- [ ] Attended school any time since September 1, 1909

**OWNERSHIP OF HOME:**

- [X] Owned or rented
- [X] Owned free or mortgaged
- [X] Farm or house
- [X] Number of farm schedule.
- [X] Whether a survivor of the Union or Confederate Army or Navy
- [X] Whether blind (both eyes).
- [X] Whether deaf and dumb.

### 1900 Census

**LOCATION:
IN CITIES: STREET; HOUSE NUMBER**

- [ ] Number of dwelling-houses in the order of visitation
- [ ] Number of family, in order of visitation
- [X] Name of each person whose place of abode on June 1, 1900, was in this family. Enter surname first, then the given name and middle initial, if any. Include every person living on June 1, 1900. Omit children born since June 1, 1900
- [X] Relationship of this person to the head of the family

**PERSONAL DESCRIPTION:**

- [X] Color or race
- [X] Sex
- [X] Date of birth: month, year
- [X] Age at last birthday (partially supported through calculation of aprox. date of birth)
- [ ] Whether single, married, widowed, or divorced
- [X] Number of years married (partially supported through calculation of aprox. date of marriage)
- [X] Mother of how many children
- [X] Number of these children living

**NATIVITY:
PLACE OF BIRTH OF EACH PERSON AND PARENTS OF EACH PERSON ENUMERATED. IF BORN IN THE UNITED STATES, GIVE THE STATE OR TERRITORY; IF OF FOREIGN BIRTH, GIVE THE COUNTRY ONLY.**

- [X] Place of birth of this person
- [ ] Place of birth of father of this person
- [ ] Place of birth of mother of this person

**CITIZENSHIP:**

- [X] Year of immigration to the United States
- [ ] Number of years in the United States
- [X] Naturalization

**OCCUPATION, TRADE OR PROFESSION:
OF EACH PERSON TEN YEARS OF AGE AND OVER:**

- [X] Occupation
- [ ] Months not employed

**EDUCATION:**

- [ ] Attended school (in months)
- [X] Can read
- [X] Can write
- [X] Can speak English

**OWNERSHIP OF HOME:**
- [X] Owned or rented
- [X] Owned free or mortgaged
- [X] Farm or house
- [X] Number of farm schedule.
 
 ### 1880 Census

**IN CITIES: NAME OF STREET; HOUSE NUMBER**

- [X] Dwelling houses numbered in order of visitation.
- [X] Families numbered in order of visitation.
- [X] The name of every person whose place of abode on the 1st day of June, 1880, was in this family.

**PERSONAL DESCRIPTION:**

- [X] Color - White, W; black, B; Mulatto, Mu; Chinese, C; Indian, I.
- [X] Sex - Males (M), females (F)
- [X] Age at last birthday prior to June 1, 1880. If under 1 year, give months in fractions, thus, 3/12. (partially supported through calculation of aprox. date of birth)
- [ ] If born within the census year, give the month.
- [X] Relationship of each person to the head of this family - whether wife, son, daughter, servant, boarder, or other.

**CIVIL CONDITION:**

- [ ] Single.
- [ ] Married.
- [ ] Widowed; divorced.
- [ ] Married during census year.

**OCCUPATION:**

- [X] Profession, occupation, or trade of each person, male or female.
- [ ] Number of months this person has been unemployed during the census year.

**HEALTH:**

- [X] Is the person (on the day of the enumerator's visit) sick or temporarily disabled, so as to be unable to attend to ordinary business or duties? Is so, what is the sickness or disability?
- [X] Blind.
- [X] Deaf and dumb.
- [X] Idiotic.
- [X] Insane
- [X] Maimed, crippled, bedridden, or otherwise disabled.

**EDUCATION:**

- [X] Attended school within the census year.
- [X] Can not read.
- [X] Can not write.

**NATIVITY:**

- [X] Place of birth of this person, naming State or Territory of United States, or the country, if of foreign birth.
- [ ] Place of birth of the father of this person, naming State or Territory of United States, or the country, if of foreign birth
- [ ] Place of birth of the mother of this person, naming State or Territory of United States, or the country, if of foreign birth

 ### 1870 Census

 - [X] Dwelling houses and number in order of visitation.
 - [X] Families numbered in the order of visitation.
 - [X] The name of every person whose place of abode on the 1st day of June, 1870, was in this family.

 **DESCRIPTION:**

 - [X] Age at last birthday. If under 1 year, give months in fractions, thus, 3/12. (partially supported through calculation of aprox. date of birth)
 - [X] Sex - Males (M), females (F).
 - [X] Color - White (W), black (B), mulatto (M), Chinese (C), Indian (I).
 - [X] Profession, occupation, or trade of each person, male or female.

**VALUE OF REAL ESTATE OWNED:**

- [X] Value of real estate.
- [X] Value of personal estate.
- [X] Place of birth, naming the state or territory of the United States, or the country, if of foreign birth.

**PARENTAGE:**

- [ ] Father of foreign birth.
- [ ] Mother of foreign birth.
- [ ] If born within the year, state month (Jan., Feb., etc.).
- [ ] If married within the year, state month (Jan., Feb., etc.)

**EDUCATION:**

- [ ] Attended school within the year.
- [X] Can not read.
- [X] Can not write.
- [X] Whether deaf and dumb, blind, insane, or idiotic.

**CONSTITUTIONAL RELATIONS:**

- [ ] Male citizens of United States of 21 years of age and upwards.
- [ ] Male citizens of United States of 21 years of age and upwards, whose right to vote is denied or abridged on other grounds than rebellion or other crime.

 ### 1860 Census

 - [X] Dwelling houses and number in order of visitation
 - [X] Families numbered in the order of visitation
 - [X] The name of every person whose usual place of abode on the 1st day of June, 1860, was in this family

 **DESCRIPTION:**

 - [X] Age (partially supported through calculation of aprox. date of birth)
 - [X] Sex
 - [X] Color - White, black, or mulatto
 - [X] Profession, occupation, or trade of each person, male or female, over 15 years of age

 **VALUE OF REAL ESTATE OWNED:**

- [X] Value of real estate
- [X] Value of personal estate
- [X] Place of birth, naming the state, territory, or country
- [ ] Married within the year
- [ ] Attended school within the year
- [X] Persons over 20 years of age who can not read and write
- [X] Whether deaf and dumb, blind, insane, idiotic, pauper or convict

### 1850 Census

- [X] Dwelling houses and number in order of visitation.
- [X] Families numbered in the order of visitation.
- [X] The name of every person whose usual place of abode on the 1st day of June, 1850, was in this family.

**DESCRIPTION**

- [X] Age (calculates approx. birth year)
- [X] Sex
- [X] Color - White, black, or mulatto.
- [X] Profession, occupation, or trade of each male person over 15 years of age.
- [X] Value of real estate owned.
- [X] Place of birth, naming the state, territory, or country.
- [ ] Married within the year.
- [ ] Attended school within the year.
- [X] Persons over 20 years of age who can not read and write.
- [X] Whether deaf and dumb, blind, insane, idiotic, pauper or convict.

## Swedish Household Examinations
Note that the program automatically adds the last name of children based on what it determines to be the father's first name.

### 1881-1885

**THE NAME COLUMN**

- [X] Personernas namn / Person's Name
- [X] Stånd / Position
- [X] Embete / State
- [X] Yrke och Näringsfång / Occupation and Trade

**FÖDELSE (BIRTH)**

- [X] År / Year
- [X] Mån. och dag. / Month and Day
- [X] Ort, (Socken i Län Stad). / Place (Parish in county, city)

**ÄKTENSKAP (MARRIAGE)**

- [X] Gift / Married
- [ ] Enkling eller Enka / Widower or Widowed

**KOPPOR (SMALLPOX)**

- [ ] Koppor / Smallpox

**HITFLYTTAD (MOVED HERE)**

- [X] Från (Socken i Län, Stad, eller pagina i Husförhörsboken). / From (Parish in county, City or page in Household examination book)
- [X] År, månad och dag / Year, month and day
- [X] Inflyttningsattestens nummer / Moving In Certificate Number

**DÖD (DEATH)**

- [X] Död / Death

**TESTS**

- [ ] Innanläsning / Reading
- [ ] Kristendomkunskap / Scripture

**BEVISTAT FÖRHÖR OCH BEGÅTT / ATTENDED EXAMINATION AND RECEIVED HOLY COMMUNION**

- [X] Years 1881-1885 for both Examination and Communion

**BEVISTAT BEVÄRINGSMÖTE / ATTENDED MILITARY MEETING**

- [ ] 1
- [ ] 2

**REMARKS**

- [ ] Frägd och särskilda anteckningar / Character and Individual Remarks

**BORTFLYTTAD / MOVING OUT**

- [X] Till socken i Län, stad eller pag. i Husförhörsboken / To parish in county, City or page in Household examination book
- [X] År, månad och dag / 	Year, month and day
- [X] Utflyttningsattestens nummer / Moving Out Certificate Number
