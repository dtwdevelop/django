import { Component, OnInit } from '@angular/core';
import {NgbModal,NgbModalRef} from "@ng-bootstrap/ng-bootstrap";
import {ApiService} from '../api.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
   modalReference:NgbModalRef;

  constructor(private modalService: NgbModal, private api: ApiService) {

  }

  open(content) {
     this.api.createUser().subscribe(data=>{console.log(data)})
     this.modalReference  = this.modalService.open(content);
     this.modalReference.result.then((result) => {

    }, (reason) => {

    });
  }
  onClose(event){

    this.modalReference.close()
  }

  ngOnInit() {

  }

}
