import {Component, Output} from '@angular/core';
import {NgbModal, NgbModalRef} from "@ng-bootstrap/ng-bootstrap";
import {ModalService} from "./modal.service";
import {trigger, state, style, animate, transition} from '@angular/animations';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [
  trigger('collapse', [
    state('open', style({
      opacity: '1',
      display: 'block',
      transform: 'translate3d(0, 0, 0)'
    })),
    state('closed',   style({
      opacity: '0',
      display: 'none',
      transform: 'translate3d(0, -100%, 0)'
    })),
    transition('closed => open', animate('200ms ease-in')),
    transition('open => closed', animate('100ms ease-out'))
  ])
]
})
export class AppComponent {
  title = 'app';
  isCollapsed = true;
  collapse:string = "closed";
  show:boolean = false;
  constructor(private modal: ModalService) {
  }

  open(content) {
    this.modal.open(content)
  }

  onClose(event) {

    this.modal.onClose(event)
  }


 toggleCollapse() {
    //this.show = !this.show
    this.collapse = this.collapse == "open" ? 'closed' : 'open';
  }
}
