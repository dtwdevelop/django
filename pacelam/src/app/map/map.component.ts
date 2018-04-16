import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  lat: number = 51.50853;
  lng: number = -0.12574;
  from:string;
  to:string;
  sourceFrom:any[]=["place","place2"];

  constructor() { }

  ngOnInit() {
  }
   From(ev){}

}
