import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  
  private baseUrl = 'http://api.localhost';

  //private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  getEmployee(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/posts/${id}`);
  }

  createEmployee(employee: Object): Observable<Object> {
    return this.http.post(`${this.baseUrl}/posts`, employee);
  }

  updateEmployee(id: number, value: any): Observable<Object> {
    return this.http.patch(`${this.baseUrl}/posts/${id}`, value);
  }

  deleteEmployee(id: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/posts/${id}`, { responseType: 'text' });
  }

  getEmployeesList(): Observable<any> {
    return this.http.get(`${this.baseUrl}/posts`);
  }

  postCeleryData(employee: Object): Observable<any>{
    
    return this.http.post(`${this.baseUrl}/tester`,employee);
  }
}