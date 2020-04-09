import { Component, OnInit } from '@angular/core';
import { UnitService } from '../../services/unit.service'
import { HttpErrorResponse } from '@angular/common/http';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';
import * as mapboxgl from 'mapbox-gl';
//declare let L;
//import '../../../../node_modules/leaflet-routing-machine/dist/leaflet-routing-machine.js'

@Component({
  selector: 'app-private-units',
  templateUrl: './private-units.component.html',
  styleUrls: ['./private-units.component.css']
})
export class PrivateUnitComponent implements OnInit {

  privateUnits: any;
  units: any = [];
  geojson: any = { 'type': 'FeatureCollection' }
  initial_coords : any = []
  constructor(private UnitService: UnitService, private router: Router) { }

  ngOnInit() {
    this.getUnits()


    //charge map
    
    //end of map

  }
  getUnits() {
    this.UnitService.getUnits().subscribe(
      data => {
        this.units = data;
        this.dataCharge()
      });
    err => { console.error(err); };

  }

  dataCharge() {
    let features : any = []
    let cont = 0
    this.units.forEach(element => {
      if(cont ==0){this.initial_coords.push(element.long, element.lat)}
      
      this.geojson
      let data_json = {
          'type': 'Feature',
          'properties': {
            'message':  ' unidad '+ element.name +' | placas: ' + element.plates + ' | coordenadas: lat=' + element.lat + ' long= ' + element.long,
            'iconSize': [60, 60]
          },
          'geometry': {
            'type': 'Point',
            'coordinates': [element.long, element.lat]
          }
        }
        cont = cont + 1
        features.push(data_json)
        this.geojson["features"] = features;
        this.chargeMap()


    });

  }
  deleteUnit(id){
    console.log('borrando esta madre')
    console.log(id)
    this.UnitService.deleteUnit(id)
  }

  chargeMap(){
    mapboxgl.accessToken = environment.mapboxKey
    var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/light-v10',
      zoom: 12,
      center: this.initial_coords
    });

    this.geojson.features.forEach(function (marker) {
      // create a DOM element for the marker
      var el = document.createElement('div');
      el.className = 'marker';
      el.style.backgroundImage =
        'url(https://placekitten.com/g/' +
        marker.properties.iconSize.join('/') +
        '/)';
      el.style.width = marker.properties.iconSize[0] + 'px';
      el.style.height = marker.properties.iconSize[1] + 'px';

      el.addEventListener('click', function () {
        window.alert(marker.properties.message);
      });

      // add marker to map
      new mapboxgl.Marker(el)
        .setLngLat(marker.geometry.coordinates)
        .addTo(map);
    });
  }


}
