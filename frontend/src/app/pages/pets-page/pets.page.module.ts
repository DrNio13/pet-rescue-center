import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { PetGraphicComponent } from './pet-graphic/pet-graphic.component';
import { PetFormComponent } from './pet-form/pet-form.component';
import { PetsPage } from './pets.page';


const routes: Routes = [
  {
    path: '',
    component: PetsPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  entryComponents: [PetFormComponent],
  declarations: [PetsPage, PetGraphicComponent, PetFormComponent],
})
export class PetsPageModule { }
