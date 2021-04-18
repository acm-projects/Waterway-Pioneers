import 'package:flutter/material.dart';
//import 'dart:convert';
//import 'package:http/http.dart' as http;
//import 'infoscreen.dart';

class ActivityList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xff08A045),
          //title: Text('Search bar goes here'),
        ),
        body: Stack(children: [
          Column(
            children: [
              Expanded(
                child: textSection,
              ),
              Expanded(
                flex: 7,
                child: LocationSection(),
              ),
              BottomNavigationBar(
                  showSelectedLabels: false,
                  showUnselectedLabels: false,
                  backgroundColor: Color(0xff08A045),
                  items: <BottomNavigationBarItem>[
                    BottomNavigationBarItem(
                        icon: Icon(Icons.search, color: Color(0xffFFFFFF)),
                        label: 'Search'),
                    BottomNavigationBarItem(
                        icon: Icon(Icons.bookmark, color: Color(0xffFFFFFF)),
                        label: 'Bookmarks'),
                    BottomNavigationBarItem(
                        icon: Icon(Icons.person_rounded,
                            color: Color(0xffFFFFFF)),
                        label: 'Profile')
                  ])
            ],
          ),
        ]));
  }
}

// areas near you
Widget textSection = Container(
  alignment: Alignment.topLeft,
  padding: const EdgeInsets.fromLTRB(20.0, 20.0, 0.0, 0.0),
  child: Text(
    'Areas Near You:',
    style: TextStyle(
      fontFamily: 'SF Pro Display',
      fontSize: 30.0,
      fontWeight: FontWeight.normal,
    ),
  ),
);

// list of locations
class CustomListItem extends StatelessWidget {
  const CustomListItem({
    Key? key,
    required this.thumbnail,
    required this.name,
    required this.city,
    required this.numMiles,
  }) : super(key: key);

  final Widget thumbnail;
  final String name;
  final String city;
  final int numMiles;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 10.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Expanded(
            flex: 2,
            child: thumbnail,
          ),
          Expanded(
            flex: 3,
            child: _LocationInformation(
              name: name,
              city: city,
              numMiles: numMiles,
            ),
          ),
          const Icon(
            Icons.arrow_forward_ios,
            size: 16.0,
          ),
        ],
      ),
    );
  }
}

class _LocationInformation extends StatelessWidget {
  const _LocationInformation({
    Key? key,
    required this.name,
    required this.city,
    required this.numMiles,
  }) : super(key: key);

  final String name;
  final String city;
  final int numMiles;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(15.0, 0.0, 5.0, 0.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          /*TextButton(
            onPressed: () => {
              Navigator.of(context)
                  .push(MaterialPageRoute(builder: (context) => InfoScreen()))
            },
            child: Text(
              name,
              style: const TextStyle(
                fontFamily: 'DM Sans',
                fontWeight: FontWeight.bold,
                fontSize: 15.0,
              ),
            ),
          ), */
          Text(
            name,
            style: const TextStyle(
              fontFamily: 'DM Sans',
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
            ),
          ),
          const Padding(padding: EdgeInsets.symmetric(vertical: 2.0)),
          Text(
            city,
            style: const TextStyle(
              fontSize: 15.0,
            ),
          ),
          const Padding(padding: EdgeInsets.symmetric(vertical: 1.0)),
          Text(
            '$numMiles miles',
            style: const TextStyle(fontSize: 15.0),
          ),
        ],
      ),
    );
  }
}

// list items
class LocationSection extends StatefulWidget {
  const LocationSection({Key? key}) : super(key: key);

  @override
  _LocationSectionState createState() => _LocationSectionState();
}

class _LocationSectionState extends State<LocationSection> {
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(15.0, 0.0, 0.0, 0.0),
      itemExtent: 106.0,
      children: <CustomListItem>[
        CustomListItem(
          city: 'Dallas, TX',
          numMiles: 7,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.blue,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Big Lake',
        ),
        CustomListItem(
          city: 'Irving, TX',
          numMiles: 14,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.yellow,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Forest Trail',
        ),
        CustomListItem(
          city: 'Plano, TX',
          numMiles: 21,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.green,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Lazy River',
        ),
        CustomListItem(
          city: 'Plano, TX',
          numMiles: 24,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.red,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Small Lake',
        ),
        CustomListItem(
          city: 'Dallas, TX',
          numMiles: 30,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.purple,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Short Trail',
        ),
        CustomListItem(
          city: 'Dallas, TX',
          numMiles: 33,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.pink,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Narrow Creek',
        ),
        CustomListItem(
          city: 'Dallas, TX',
          numMiles: 7,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.blue,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Big Lake',
        ),
        CustomListItem(
          city: 'Irving, TX',
          numMiles: 14,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.yellow,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Forest Trail',
        ),
        CustomListItem(
          city: 'Plano, TX',
          numMiles: 21,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.green,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Lazy River',
        ),
        CustomListItem(
          city: 'Plano, TX',
          numMiles: 24,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.red,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Small Lake',
        ),
        CustomListItem(
          city: 'Dallas, TX',
          numMiles: 30,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.purple,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Short Trail',
        ),
        CustomListItem(
          city: 'Dallas, TX',
          numMiles: 33,
          thumbnail: Container(
            decoration: const BoxDecoration(
                color: Colors.pink,
                borderRadius: BorderRadius.all(Radius.circular(15))),
          ),
          name: 'Narrow Creek',
        ),
      ],
    );
  }
}
