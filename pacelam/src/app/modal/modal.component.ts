import {Component, OnInit, Output, EventEmitter} from '@angular/core';
import {FormBuilder,FormControl, FormGroup,Validators} from '@angular/forms';
import {ApiService} from '../api.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';


@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent implements OnInit {
  @Output() onClose = new EventEmitter<boolean>();
  clientForm :FormGroup

  constructor(private form:FormBuilder ,private api:ApiService){
   this.createForm()

  }
  ngOnInit() {
  }

  createForm(){
    this.clientForm  = this.form.group({
      username: ['',Validators.required],
      password: ['',Validators.required],
      email: ['',Validators.required],
      first_name: [''],
      last_name: [''],
      password_r: ['',Validators.required],
      agree: ['',Validators.required]

    })
  }
  Submit(){
    if(this.clientForm.valid){
       this.api.createUser(this.clientForm.value).subscribe(data=>{console.log(data)})

      console.log("Form sent")
      this.onClose.emit(true)
    }
  }


  close(d) {

    this.onClose.emit(true)
  }

}
