# /deploy

Prepare and execute the project deployment.

## Usage

```
/deploy [environment: dev|staging|prod]
```

## Instructions

1. **Pre-deployment checks**:
   - Tests pass (`/test`)
   - No hardcoded secrets
   - Environment variables configured
   - Build succeeds

2. **Deployment**:
   - Run the appropriate pipeline for the target environment
   - Always confirm before deploying to **production**

3. **Post-deployment**:
   - Verify the service responds
   - Check logs for errors

> ⚠️ Always ask for explicit confirmation before any production deployment.
