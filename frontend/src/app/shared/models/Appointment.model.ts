export class Speciality {
  id: string;
  name: string;
}

export class Doctor {
  id: string;
  name: string;
  crm: number;
  speciality: Speciality;
}

export class Appointment {
  id: string;
  doctor: Doctor;
  day: string;
  time: string;
  // tslint:disable-next-line:variable-name
  created_at: string;
}

export class AvailableTime {
  id: string;
  day: string;
  time: string;
  Doctor: string;
  Patient: string;
}

export class Schedule {
  id: string;
  doctor: string;
  day: string;
  // tslint:disable-next-line:variable-name
  available_times: AvailableTime[];
}

export class AuthenticationResponse {
  token: string;
}

export class UserData {
  name: string;
}
