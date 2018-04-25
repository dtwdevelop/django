import { Component, OnInit } from '@angular/core';
import {ApiService} from "../api.service";

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
  sourceFrom:any[]=[];

  constructor(private api:ApiService) { }

  From(event){
     if(event.target.value.length > 4){

      this.api.findCity(event.target.value).subscribe(data=> {
        data = JSON.parse(data)
        data['predictions'].map(val=>{


          this.sourceFrom.push(val.description)

        })

      });
    }
  }
  ngOnInit() {
  }


}
