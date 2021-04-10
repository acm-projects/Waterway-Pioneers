import 'package:flutter/material.dart';

class InfoScreen extends StatefulWidget {
  @override
  _InfoScreenState createState() => _InfoScreenState();
}

class _InfoScreenState extends State<InfoScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(backgroundColor: Color(0xff08A045)),
        body: Stack(
          children: [
            Column(
              children: [
                Expanded(
                  child: Text('test'), // add rest in later
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
            )
          ],
        ));
  }
}
