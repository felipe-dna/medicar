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
  doctor_id: string;
  patient_id: string;
  day: string;
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
    doctor_id: null,
    patient_id: window.localStorage.getItem('userId'),
    day: null,
    time: null
  };
  public formReady = false;

  constructor(
    public apiService: ApiService,
    public dialogRef: MatDialogRef<AppointmentFormComponent>,
    @Inject(MAT_DIALOG_DATA) public appointmentData: AppointmentData
  ) { }

  ngOnInit(): void {
    this.getMedicalSpecialties();
  }

  closeModal(): void {
    this.dialogRef.close();
  }

  addNewAppointment(event): void  {
    event.preventDefault();
    this.createNewAppointment(this.newAppointment);
  }

  onSelectChanges(event): void {
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
        this.newAppointment.doctor_id = value;
        this.getDoctorsSchedule(value);

        dateInput.removeAttribute('disabled');
        break;
      }
      case 'date': {
        this.newAppointment.day = value;
        this.getDoctorsSchedule(this.newAppointment.doctor_id, value);
        timeInput.removeAttribute('disabled');
        break;
      }
      case 'time': {
        this.newAppointment.time = value;
        this.formReady = true;
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
      date ? this.availableTimes = data[0].available_times : this.schedules = data;
    });
  }
  public createNewAppointment(bodyParameters: AppointmentBodyParameters): void {
    this.apiService.createNewAppointment(bodyParameters).subscribe(() => {
      window.location.reload();
    });
  }
}
