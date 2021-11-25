int Yang()
{
   double bkg = 454.59;
   double sig = 101.63 ;
   printf("%f\n",bkg);
   double lumi = 1;

   bkg *= lumi;
   sig *= lumi;

   double xMin = bkg - TMath::Sqrt(sig+bkg) * 50.0;
   double xMax = sig+bkg + TMath::Sqrt(sig+bkg) * 50.0;
   if(xMin < 0.0) xMin = 0.0;
   cout << "Space " << xMin << " " << xMax << endl;


   TF1 *f1 = new TF1("f1","TMath::Poisson(x,[0])",xMin,xMax);
   f1->SetParameter(0,bkg);

   TH1D* h1 = new TH1D("h1","h1",10000, sig+bkg,xMax);
   h1->Eval(f1);
   h1->SetFillColor(kRed);
   h1->SetFillStyle(3001);

   TCanvas* c1 = new TCanvas();
   c1->SetLogy();
   c1->SetGridx();
   c1->SetGridy();
   f1->Draw();
   h1->Draw("sameHIST");

   double pVal =  1.0 - f1->Integral(xMin,sig+bkg);
   //double pVal =  2.87 / 10000000.0 ;
   double sigma = ROOT::Math::normal_quantile_c(pVal, 1);
   cout <<  " p-value " << pVal << " sigma " << sigma << endl;
   return 0;
}
