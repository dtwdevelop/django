import { Component, OnInit } from '@angular/core';
import {ModalService} from "../modal.service";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  constructor(private modal:ModalService) {
    }
    open(content) {
    this.modal.open(content)
  }
  onClose(event){

   this.modal.onClose(event)
  }

  ngOnInit() {

  }

}
