PROJECT_ID=alien-airfoil-417901
WIP=github-wi
SVC=github-action
GITHUB_USER_NAME=DanielMontecino
GITHUB_REPOSITORY=fast-api-deployment

# Create WIP to allow Github to authenticate with GCP
gcloud iam workload-identity-pools create $WIP \
    --location="global" \
    --description="Workload Identity Pools for GitHub" \
    --display-name="$WIP" \
    --project $PROJECT_ID

# Create an OIDC provider for Workload Identity Pool (github-wif) from the below gcloud command
gcloud iam workload-identity-pools providers create-oidc github-oidc \
--location="global" --workload-identity-pool="$WIP"  \
--issuer-uri="https://token.actions.githubusercontent.com" \
--attribute-mapping="attribute.actor=assertion.actor,google.subject=assertion.sub,attribute.repository=assertion.repository" \
--project $PROJECT_ID

# Create a Service Account for our Workload Identity Pool
gcloud iam service-accounts create $SVC \
--display-name="Service account used by github WIF" \
--project $PROJECT_ID

# grant your service account an IAM role on your project
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SVC@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/iam.serviceAccountTokenCreator"

# Attach IAM Role(Workload Identity User) to service account
gcloud iam service-accounts add-iam-policy-binding $SVC@$PROJECT_ID.iam.gserviceaccount.com \
--project=$PROJECT_ID \
--role="roles/iam.workloadIdentityUser" \
--member="principalSet://iam.googleapis.com/projects/797982961252/locations/global/workloadIdentityPools/$WIP/attribute.repository/$GITHUB_USER_NAME/$GITHUB_REPOSITORY"

