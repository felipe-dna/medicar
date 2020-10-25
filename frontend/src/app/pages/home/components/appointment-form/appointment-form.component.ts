import {Component, Inject, OnInit} from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import {ApiService} from '../../../../shared/service/api.service';
import {Doctor, Speciality} from '../../../../shared/models/Appointment.model';

export interface AppointmentData {
  speciality: string;
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
  public specialties: Speciality[];
  public doctors: Doctor[];

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
}
