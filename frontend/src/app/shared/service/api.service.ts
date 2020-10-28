import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Appointment, AuthenticationResponse, Doctor, Schedule, Speciality, UserData } from '../models/Appointment.model';

import { environment } from '../../../environments/environment';
import {AppointmentBodyParameters} from '../../pages/home/components/appointment-form/appointment-form.component';

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  private apiUrl: string = environment.apiUrl;

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    })
  };

  httpAuthorizedOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: `token ${window.localStorage.getItem('token')}`
    })
  };

  constructor(
        private httpClient: HttpClient
  ) {}

  public getMedicalAppointments(): Observable<Appointment[]> {
    return this.httpClient.get<Appointment[]>(`${this.apiUrl}/appointments`, this.httpAuthorizedOptions);
  }

  public getMedicalSpecialties(): Observable<Speciality[]> {
    return this.httpClient.get<Speciality[]>(`${this.apiUrl}/specialties`, this.httpAuthorizedOptions);
  }

  public getDoctorsBySpeciality(specialityId: string): Observable<Doctor[]> {
    return this.httpClient.get<Doctor[]>(`${this.apiUrl}/doctors?speciality=${specialityId}`, this.httpAuthorizedOptions);
  }

  public getDoctorSchedulesByDate(doctorId: string, date: string = null): Observable<Schedule[]> {
    let url: string;
    (date !== null ?
        url = `${this.apiUrl}/doctors/${doctorId}/schedules?date=${date}` :
        url = `${this.apiUrl}/doctors/${doctorId}/schedules`
      );
    return this.httpClient.get<Schedule[]>(url, this.httpAuthorizedOptions);
  }

  public authenticateUser(credentials: {}): Observable<AuthenticationResponse> {
    return this.httpClient
      .post<AuthenticationResponse>(`${this.apiUrl}/users/login`, credentials, this.httpOptions);
  }

  public getUserData(): Observable<UserData> {
    return this.httpClient.get<UserData>(`${this.apiUrl}/users`, this.httpAuthorizedOptions);
  }

  public createNewAppointment(bodyParameters: AppointmentBodyParameters): Observable<Appointment[]> {
    return this.httpClient.post<Appointment[]>(`${this.apiUrl}/appointments`, bodyParameters, this.httpAuthorizedOptions);
  }

  public deleteAppointment(appointmentId: string): Observable<null> {
    return this.httpClient.delete<null>(`${this.apiUrl}/appointments/${appointmentId}`, this.httpAuthorizedOptions);
  }
}
