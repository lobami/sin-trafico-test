import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class UnitService {

  private URL = 'http://localhost:8000/api/1';
  constructor(private http: HttpClient) { }

  getUnits() {
    return this.http.get(this.URL + '/users/' + localStorage.getItem('user_id') + '/units/');
  }
  deleteUnit(id:any) {
    return this.http.get(this.URL + '/users/' + localStorage.getItem('user_id') + '/units/');
    //return this.http.get(this.URL + '/units/' + id +'/');
  }

  

}
