import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PrivateUnitComponent } from './private-units.component';

describe('PrivateTasksComponent', () => {
  let component: PrivateUnitComponent;
  let fixture: ComponentFixture<PrivateUnitComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PrivateUnitComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PrivateUnitComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
