import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Appointment, AuthenticationResponse, Doctor, Schedule, Speciality} from '../models/Appointment.model';

import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  private apiUrl: string = environment.apiUrl;

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

  public getDoctorsBySpeciality(specialityId: string): Observable<Doctor[]> {
    return this.httpClient.get<Doctor[]>(`${this.apiUrl}/doctors?speciality=${specialityId}`, this.httpOptions);
  }

  public getDoctorSchedulesByDate(doctorId: string, date: string = null): Observable<Schedule[]> {
    let url: string;
    (date !== null ?
        url = `${this.apiUrl}/doctors/${doctorId}/schedules?date=${date}` :
        url = `${this.apiUrl}/doctors/${doctorId}/schedules`
      );
    return this.httpClient.get<Schedule[]>(url, this.httpOptions);
  }

  public authenticateUser(credentials: {}): Observable<AuthenticationResponse> {
    return this.httpClient.post<AuthenticationResponse>(
      `${this.apiUrl}/users/login`,
      credentials,
      this.httpOptions,
    );
  }
}
