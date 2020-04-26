import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-enquiries-page',
  templateUrl: './enquiries-page.page.html',
  styleUrls: ['./enquiries-page.page.scss'],
})
export class EnquiriesPage implements OnInit {


  constructor(public auth: AuthService) {

  }

  ngOnInit() {
  }

}
