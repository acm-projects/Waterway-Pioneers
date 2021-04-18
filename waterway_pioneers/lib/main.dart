import 'package:flutter/material.dart';
//import 'activitylist.dart';
//import 'map.dart';
import 'infoscreen.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: InfoScreen(),
    );
  }
}
