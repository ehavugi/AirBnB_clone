# VAirBnB\_clone
Initial work on Alx AirBnB clone

## Console interaction

The console manages interaction with json base data storage.
Sample interaction with console is added below

help --> list all commands

help command --> explain what command does

```console
root@b41d5e6d03f4:~/AirBnB_clone# ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
root@b41d5e6d03f4:~/AirBnB_clone# ./console.py 
(hbnb) quit
root@b41d5e6d03f4:~/AirBnB_clone# ./console.py 
(hbnb) help show

        print string representation of an instance based on class name and id
        show BaseModel 1234-1234-1234
        
(hbnb) help create

        test create model.

        
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
return all
(hbnb) 
(hbnb) count
*** Unknown syntax: count
(hbnb) count Place
*** Unknown syntax: count Place
(hbnb) User.count()
12
(hbnb) create User
3caac475-ecda-4ec9-9a8e-7a2fd17167d4
(hbnb) User.count()
13
(hbnb) Place.count()
9
(hbnb) Create Place
*** Unknown syntax: Create Place
(hbnb) create Place
c1653e9d-d52a-4ef2-bd37-c752a234dceb
(hbnb) Place.count()
10
(hbnb) destroy Place c1653e9d-d52a-4ef2-bd37-c752a234dceb
(hbnb) Place.count()
9
(hbnb) 

(hbnb) all Place
["[Place] (2f89bf8b-4fc6-4fbb-aa74-9eb75fbcb77f) {'id': '2f89bf8b-4fc6-4fbb-aa74-9eb75fbcb77f', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 533975), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 533975)}", "[Place] (029b3f91-d352-4a30-8533-b4f62649a787) {'id': '029b3f91-d352-4a30-8533-b4f62649a787', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 537294), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 537312)}", "[Place] (a1709f59-ed68-4314-82fa-b319d0991efb) {'id': 'a1709f59-ed68-4314-82fa-b319d0991efb', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 631410), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 631428)}", "[Place] (0a57dc01-5d3f-4bf4-b10c-5c0cf2386b0b) {'id': '0a57dc01-5d3f-4bf4-b10c-5c0cf2386b0b', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 731305), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 731305)}", "[Place] (9f87a169-005f-4ae6-850a-d80bc9477644) {'id': '9f87a169-005f-4ae6-850a-d80bc9477644', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 735500), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 735518)}", "[Place] (e44a4f3a-97c9-46d5-a95c-2a0bb1bc51ec) {'id': 'e44a4f3a-97c9-46d5-a95c-2a0bb1bc51ec', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 833925), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 833945)}", "[Place] (ba207755-3c06-4e33-9f2a-391c51b9fe8e) {'id': 'ba207755-3c06-4e33-9f2a-391c51b9fe8e', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 18, 939621), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 18, 939621)}", "[Place] (24cfc1bf-fa9b-4c46-9492-23bf5467b5f1) {'id': '24cfc1bf-fa9b-4c46-9492-23bf5467b5f1', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 35744), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 35767)}", "[Place] (8645e077-658e-4df1-9e42-13d43d55f67f) {'id': '8645e077-658e-4df1-9e42-13d43d55f67f', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 143844), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 143862)}"]
(hbnb) all Amenity
["[Amenity] (a0ff39d5-3fed-4790-87f0-beacb3dd6980) {'id': 'a0ff39d5-3fed-4790-87f0-beacb3dd6980', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 531317), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 636586)}", "[Amenity] (28fc56a9-a33f-44de-b1fa-14ff75826861) {'id': '28fc56a9-a33f-44de-b1fa-14ff75826861', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 539142), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 539159)}", "[Amenity] (916e4b74-9be4-4e37-88ec-e11ccec6ba2c) {'id': '916e4b74-9be4-4e37-88ec-e11ccec6ba2c', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 633458), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 36, 633475)}", "[Amenity] (1901272c-2f7f-4b47-9a2b-e7d579f20ff3) {'id': '1901272c-2f7f-4b47-9a2b-e7d579f20ff3', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 639482), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 841058)}", "[Amenity] (6319d7d1-1ba8-4885-b3ce-7c1ab409a4e4) {'id': '6319d7d1-1ba8-4885-b3ce-7c1ab409a4e4', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 738630), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 738648)}", "[Amenity] (3759dea0-733a-471c-81f0-ef39c08da5c3) {'id': '3759dea0-733a-471c-81f0-ef39c08da5c3', 'created_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 836593), 'updated_at': datetime.datetime(2023, 3, 13, 20, 8, 37, 836612)}", "[Amenity] (5e0ff4e5-dd30-4874-b16e-21a214191747) {'id': '5e0ff4e5-dd30-4874-b16e-21a214191747', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 18, 935544), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 332079)}", "[Amenity] (04b5dfb3-16cc-4ef0-a296-bfe53fccf36b) {'id': '04b5dfb3-16cc-4ef0-a296-bfe53fccf36b', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 39722), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 39746)}", "[Amenity] (630ca03b-ae4b-4601-b8ff-bc92843e0996) {'id': '630ca03b-ae4b-4601-b8ff-bc92843e0996', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 233944), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 233969)}"]

(hbnb) show Place 8645e077-658e-4df1-9e42-13d43d55f67f
[Place] (8645e077-658e-4df1-9e42-13d43d55f67f) {'id': '8645e077-658e-4df1-9e42-13d43d55f67f', 'created_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 143844), 'updated_at': datetime.datetime(2023, 3, 13, 20, 9, 19, 143862)}

```

--> checkmarks reflect ALX system checked for previous commits.
(may not be updated for each commit)

## Mandatory
- [x] README, AUTHORS
- [x] Be pycodestyle compliant!
- [x] Unittests
- [x] BaseModel
- [x] Create BaseModel from dictionary
- [ ] Store first object
- [x] Console 0.0.1
- [x] Console 0.1
- [x] First User
- [x] More classes!
- [x] Console 1.0
## Advanced 
- [x]  All instances by class name
- [x] Count instances
- [x] Show
- [x] Destroy
- [x] Update
- [x] Update from dictionary
- [ ] Unittests for the Console!

