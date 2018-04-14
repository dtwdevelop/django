import {Component, OnInit, EventEmitter, Output} from '@angular/core';
import {FormBuilder, FormGroup,Validators} from '@angular/forms';
import {NgbModal,NgbModalRef} from "@ng-bootstrap/ng-bootstrap";


@Component({
  selector: 'app-loginmodal',
  templateUrl: './loginmodal.component.html',
  styleUrls: ['./loginmodal.component.css']
})
export class LoginmodalComponent implements OnInit {
  formLogin:FormGroup
  modalReference:NgbModalRef
  @Output() onClose = new EventEmitter<boolean>();

  constructor(private fb:FormBuilder ,private modalService:NgbModal) {
    this.createForm()
  }
  createForm(){
    this.formLogin  =this.fb.group(
      {
        username:['',Validators.required],
        password:['',Validators.required]
      }
    )
  }

  Submit(){

  }


  ngOnInit() {
  }

  close(d) {

    this.onClose.emit(true)
  }

}
