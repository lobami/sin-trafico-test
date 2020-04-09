import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
// Components
import { TasksComponent } from './components/tasks/tasks.component';
import { PrivateTasksComponent } from './components/private-tasks/private-tasks.component';
import { PrivateUnitComponent } from './components/units/private-units.component';
import { SigninComponent } from './components/signin/signin.component';
import { SignupComponent } from './components/signup/signup.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/units',
    pathMatch: 'full'
  },
  {
    path: 'tasks',
    component: TasksComponent
  },
  {
    path: 'units',
    component: PrivateUnitComponent
  },
  {
    path: 'private',
    component: PrivateTasksComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'signin',
    component: SigninComponent
  },
  {
    path: 'signup',
    component: SignupComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
