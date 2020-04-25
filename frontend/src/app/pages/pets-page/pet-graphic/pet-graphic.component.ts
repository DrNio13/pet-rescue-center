import { Component, OnInit, Input } from '@angular/core';
import { PetsService } from 'src/app/services/pets.service';

@Component({
  selector: 'app-pet-graphic',
  templateUrl: './pet-graphic.component.html',
  styleUrls: ['./pet-graphic.component.scss'],
})
export class PetGraphicComponent implements OnInit {
  @Input() pet: any;

  constructor() { }

  ngOnInit() { }

}
