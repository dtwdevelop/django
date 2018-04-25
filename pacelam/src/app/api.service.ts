import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders,} from '@angular/common/http';
import {RequestOptions, Request, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { ErrorObservable } from 'rxjs/observable/ErrorObservable';
import {catchError, retry, tap} from 'rxjs/operators';
import {Client} from './client/Client';
@Injectable()
export class ApiService {


  constructor(private http:HttpClient) { }

  createUser(datas=null):Observable<Client>{
    let user:any  =  {
     "user": {
       "username" : datas.username,
        "password": datas.password,
        "first_name": datas.first_name,
        "last_name": datas.last_name,
        "email": datas.email,
     },
     "name" : datas.username
    }
  const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};
    // if not user.id wrong
    let  url:string  ="http://localhost:8000/client/"
    return this.http.post(url,user,httpOptions).pipe(tap(
     data =>console.log(data),
      //catchError(this.Error(data))
    ))
  }

  Error  (data):any{
    console.log(data)

  }
  findCity(city:string):any{

      const httpOptions = {
          headers: new HttpHeaders({
              'Content-Type':  'application/json',
              // 'Access-Control-Allow-Origin' : '*',
              // 'Access-Control-Allow-Credentials' :' false',
              // 'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
            // 'Origin' : 'http://www.someorigin.com'
          })
      };
      let  url:string ="http://localhost:8000/map/?city="+city+"";
      return this.http.get(url,httpOptions).map(res => res) ;


  }

}
