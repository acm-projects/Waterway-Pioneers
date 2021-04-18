import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong/latlong.dart';
import 'dart:ui';

class Map extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MapState();
}

class _MapState extends State<Map> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: Color(0xff08A045), title: new Text('Trail Map')),
      body: Column(
        children: [
          Container(
            height: 623,
            child: new FlutterMap(
                options: new MapOptions(
                    center: new LatLng(32.7767, -96.7970), minZoom: 7.0),
                layers: [
                  new TileLayerOptions(
                      urlTemplate:
                          "https://api.mapbox.com/styles/v1/backchris27/ckmjjijd12bjg17s6ek306esg/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiYmFja2NocmlzMjciLCJhIjoiY2ttM3BjNm9mMGF3czJwbXkzdG5nbzkydiJ9.lL-O8cMdpd2P3an3bblZdA",
                      additionalOptions: {
                        'accessToken':
                            'pk.eyJ1IjoiYmFja2NocmlzMjciLCJhIjoiY2ttM3BjNm9mMGF3czJwbXkzdG5nbzkydiJ9.lL-O8cMdpd2P3an3bblZdA',
                        'id': 'mapbox.mapbox-streets-v7'
                      }),
                  new MarkerLayerOptions(markers: [
                    new Marker(
                        width: 45.0,
                        height: 45.0,
                        point: new LatLng(32.9858, -96.7501),
                        builder: (context) => new Container(
                              child: IconButton(
                                icon: Icon(Icons.location_on),
                                color: Colors.red,
                                iconSize: 45.0,
                                onPressed: () {
                                  print('Marker tapped');
                                },
                              ),
                            ))
                  ]),
                ]),
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
                    icon: Icon(Icons.person_rounded, color: Color(0xffFFFFFF)),
                    label: 'Profile')
              ])
        ],
      ),
    );
  }
}
