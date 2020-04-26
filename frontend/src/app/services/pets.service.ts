import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';
import { Observable, merge } from 'rxjs';
import { flatten } from '@angular/compiler';

@Injectable({
  providedIn: 'root'
})
export class PetsService {
  public url = environment.apiServerUrl;

  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization', `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getPets() {
    if (this.auth.can('get:pets-detail')) {
      return this.http.get(this.url + '/pets-detail', this.getHeaders());

    } else {
      return this.http.get(this.url + '/pets', this.getHeaders());
    }
  }

  savePet(pet: any) {
    if (pet.id >= 0) { // patch
      this.http.patch(this.url + '/pets/' + pet.id, pet, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            // this.petsToItems(res.pets);
          }
        });
    } else { // insert
      this.http.post(this.url + '/pets', pet, this.getHeaders())
        .subscribe((res: any) => {
          if (res.success) {
            // this.petsToItems(res.pets);
          }
        });
    }

  }

  deletePet(pet: any) {
    this.http.delete(this.url + '/pets/' + pet.id, this.getHeaders())
      .subscribe((res: any) => {

      });
  }


}
