export class AppointmentDoctorSpeciality {
  id: string;
  name: string;
}

export class AppointmentDoctor {
  id: string;
  name: string;
  crm: number;
  speciality: AppointmentDoctorSpeciality;
}

export class Appointment {
  id: string;
  time: string;
  doctor: AppointmentDoctor;
}

export class Speciality {
  id: string;
  name: string;
}

export class Doctor {
  id: string;
  name: string;
  crm: number;
  email: string;
  phone: string;
  speciality: Speciality;
}
