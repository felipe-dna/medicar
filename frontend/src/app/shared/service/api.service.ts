import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Appointment, Speciality } from '../models/Appointment.model';

import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  apiUrl: string = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: 'Token 2f19c8d5b3ef97e08f5328c6c6bdefaaff769a80',
    })
  };

  constructor(
        private httpClient: HttpClient
  ) {}

  public getMedicalAppointments(): Observable<Appointment[]> {
    return this.httpClient.get<Appointment[]>(`${this.apiUrl}/appointments`, this.httpOptions);
  }

  public getMedicalSpecialties(): Observable<Speciality[]> {
    return this.httpClient.get<Speciality[]>(`${this.apiUrl}/specialties`, this.httpOptions);
  }
}
