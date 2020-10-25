import {Component, Inject, OnInit} from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { ApiService } from '../../../../shared/service/api.service';
import { AvailableTime, Doctor, Schedule, Speciality } from '../../../../shared/models/Appointment.model';

export interface AppointmentData {
  speciality: string;
  doctor: string;
  date: string;
  time: string;
}

export interface AppointmentBodyParameters {
  doctor: string;
  date: string;
  time: string;
}

@Component({
  selector: 'app-appointment-form',
  templateUrl: './appointment-form.component.html',
  styleUrls: ['./appointment-form.component.css']
})
export class AppointmentFormComponent implements OnInit {
  // Form needed data;
  public specialties: Speciality[];
  public doctors: Doctor[];
  public schedules: Schedule[];
  public availableTimes: AvailableTime[];
  public newAppointment: AppointmentBodyParameters = {
    doctor: null,
    date: null,
    time: null
  };

  constructor(
    public apiService: ApiService,
    public dialogRef: MatDialogRef<AppointmentFormComponent>,
    @Inject(MAT_DIALOG_DATA) public appointmentData: AppointmentData
  ) { }

  ngOnInit(): void {
    this.getMedicalSpecialties();
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  onSelectChanges(event): void {
    const specialityInput = document.querySelector('#speciality');
    const doctorInput = document.querySelector('#doctor');
    const dateInput = document.querySelector('#date');
    const timeInput = document.querySelector('#time');

    const targetInput = event.target;
    const value = event.target.value;

    switch (targetInput.id) {
      case 'speciality': {
        this.getDoctors(value);
        doctorInput.removeAttribute('disabled');
        break;
      }
      case 'doctor': {
        this.newAppointment.doctor = value;
        this.getDoctorsSchedule(value);
        dateInput.removeAttribute('disabled');
        break;
      }
      case 'date': {
        // @ts-ignore
        this.getDoctorsSchedule(doctorInput.value, value);
        this.availableTimes = this.schedules[0].available_times;
        timeInput.removeAttribute('disabled');
        this.newAppointment.date = value;
        break;
      }
      case 'time': {
        this.newAppointment.time = value;
        console.log(this.newAppointment);
        break;
      }
    }
  }

  getMedicalSpecialties(): void{
    this.apiService.getMedicalSpecialties().subscribe(data => this.specialties = data);
  }
  getDoctors(specialityId: string): void {
    this.apiService.getDoctorsBySpeciality(specialityId).subscribe(data => {
      this.doctors = data;
    });
  }
  getDoctorsSchedule(doctorId: string, date: string = null): void {
    this.apiService.getDoctorSchedulesByDate(doctorId, date).subscribe(data => {
      this.schedules = data;
    });
  }
}
